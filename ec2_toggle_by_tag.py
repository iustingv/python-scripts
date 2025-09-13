import argparse
import boto3
from botocore.exceptions import ClientError

def parse_args():
    p = argparse.ArgumentParser(description="Start/Stop EC2 instances by tag")
    p.add_argument("action", choices=["start", "stop"], help="What to do")
    p.add_argument("tag", help="Tag filter in the form Key=Value, e.g. Environment=Dev")
    p.add_argument("--region", default=None, help="Override region (optional)")
    p.add_argument("--apply", action="store_true", help="Actually perform the action (not just DryRun)")
    return p.parse_args()

def main():
    args = parse_args()

    # Split tag "Key=Value"
    if "=" not in args.tag:
        print("Tag must be Key=Value, e.g. Environment=Dev")
        return
    tag_key, tag_val = args.tag.split("=", 1)

    ec2 = boto3.client("ec2", region_name=args.region)

    # Find instances matching the tag
    filters = [{"Name": f"tag:{tag_key}", "Values": [tag_val]}]
    resp = ec2.describe_instances(Filters=filters)

    instance_ids = []
    for res in resp.get("Reservations", []):
        for inst in res.get("Instances", []):
            instance_ids.append(inst["InstanceId"])

    if not instance_ids:
        print(f"No instances found with tag {tag_key}={tag_val}")
        return

    print(f"Target instances: {', '.join(instance_ids)}")

    # Choose API call
    api = ec2.start_instances if args.action == "start" else ec2.stop_instances

    # First do a DryRun for safety unless --apply is used
    try:
        api(InstanceIds=instance_ids, DryRun=not args.apply)
        if args.apply:
            print(f"✔ Requested to {args.action} instances.")
        else:
            print(f"(DryRun) Permission check passed to {args.action}. Re-run with --apply to execute.")
    except ClientError as e:
        # DryRun passes by raising DryRunOperation if allowed; handle AccessDenied, etc.
        code = e.response.get("Error", {}).get("Code", "")
        msg = e.response.get("Error", {}).get("Message", "")

        if code == "DryRunOperation":
            # Allowed to perform the action, but DryRun=True prevented changes
            print(f"(DryRun) Allowed to {args.action}. Re-run with --apply to actually do it.")
            return

        # NEW: graceful read-only behavior (no perms -> exit cleanly without looking like an error)
        if code in {"UnauthorizedOperation", "AccessDenied", "AccessDeniedException"}:
            print("ℹ️ Read-only mode: no permissions to start/stop. Matched instances shown above; no action taken.")
            return

        # Any other unexpected AWS error
        print(f"❌ AWS error: {code} - {msg}")

if __name__ == "__main__":
    main()

