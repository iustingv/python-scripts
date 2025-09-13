import argparse
import csv
from datetime import datetime, timezone
import boto3

def parse_args():
    p = argparse.ArgumentParser(description="EC2 Usage Tracker (current uptime)")
    p.add_argument("--tag", help="Filter by tag: Key=Value (e.g. Project=App1)", default=None)
    p.add_argument("--region", help="AWS region override (optional)")
    p.add_argument("--out", help="Output CSV file", default="ec2_report.csv")
    return p.parse_args()

def main():
    args = parse_args()
    ec2 = boto3.client("ec2", region_name=args.region)

    # Build filters if a tag was provided
    filters = []
    if args.tag:
        if "=" not in args.tag:
            print("Tag must be Key=Value (e.g. Project=App1)")
            return
        k, v = args.tag.split("=", 1)
        filters.append({"Name": f"tag:{k}", "Values": [v]})

    # Use paginator to cover all instances
    paginator = ec2.get_paginator("describe_instances")
    pages = paginator.paginate(Filters=filters) if filters else paginator.paginate()

    rows = []
    now = datetime.now(timezone.utc)

    for page in pages:
        for reservation in page.get("Reservations", []):
            for inst in reservation.get("Instances", []):
                instance_id = inst.get("InstanceId", "")
                state = inst.get("State", {}).get("Name", "")
                itype = inst.get("InstanceType", "")
                region = ec2.meta.region_name
                launch_time = inst.get("LaunchTime")  # timezone-aware datetime
                # Name tag (optional)
                name = ""
                for t in inst.get("Tags", []) or []:
                    if t.get("Key") == "Name":
                        name = t.get("Value", "")
                        break

                # Compute current uptime (hours) if running; else 0
                uptime_hours = 0.0
                if state == "running" and isinstance(launch_time, datetime):
                    uptime_hours = (now - launch_time).total_seconds() / 3600.0

                rows.append({
                    "InstanceId": instance_id,
                    "Name": name,
                    "State": state,
                    "Type": itype,
                    "Region": region,
                    "LaunchTime": launch_time.isoformat() if isinstance(launch_time, datetime) else "",
                    "UptimeHours": f"{uptime_hours:.2f}",
                })

    # Write CSV
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["InstanceId","Name","State","Type","Region","LaunchTime","UptimeHours"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Wrote {len(rows)} rows to {args.out}")

if __name__ == "__main__":
    main()

