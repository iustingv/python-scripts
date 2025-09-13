import boto3

# Create an S3 client (boto3 will read your ~/.aws/credentials automatically)
s3 = boto3.client("s3")

# Get list of buckets
response = s3.list_buckets()

print("✅ Your S3 Buckets:")
for bucket in response["Buckets"]:
    print(f" - {bucket['Name']} (created: {bucket['CreationDate']})")

