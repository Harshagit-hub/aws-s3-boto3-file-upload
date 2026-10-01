import boto3
s3 = boto3.client("s3", region_name="REGION")

s3.upload_file(
    "message.txt", 
    "boto3-s3-demo-bucket-2026",
    "message.txt"
)

print("File uploaded")
data = s3.head_object(
    Bucket="boto3-s3-demo-bucket-2026",
    Key="message.txt"
)

print("File size:", data["ContentLength"], "bytes")
print("Last Modified:", data["LastModified"])
