import boto3

# 1) Make an EC2 client.
#    boto3 reads your credentials from ~/.aws/credentials and region from ~/.aws/config
ec2 = boto3.client("ec2")  # you can force a region: boto3.client("ec2", region_name="us-east-1")

# 2) Use a paginator so it works even if you have many instances.
paginator = ec2.get_paginator("describe_instances")

print("InstanceId\tName\tState\tType\tRegion")

# 3) Go through every page of results, every reservation, every instance
for page in paginator.paginate():
    for reservation in page.get("Reservations", []):
        for inst in reservation.get("Instances", []):
            instance_id = inst.get("InstanceId", "")
            state = inst.get("State", {}).get("Name", "")
            itype = inst.get("InstanceType", "")
            region = ec2.meta.region_name  # which region this client is talking to

            # Find the Name tag if it exists
            name = ""
            for t in inst.get("Tags", []):
                if t.get("Key") == "Name":
                    name = t.get("Value", "")
                    break

            print(f"{instance_id}\t{name}\t{state}\t{itype}\t{region}")

