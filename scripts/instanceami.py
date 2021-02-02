import boto3
import os

system_name = os.getenv('HOSTNAME')
print("hostname: " +system_name)

client = boto3.client("ec2", region_name="us-east-2")
instance=["id"]

#hostname=`curl http://169.254.169.254/latest/meta-data/local-hostname`

response = client.describe_instances(InstanceIds=instance)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance: " + instance['InstanceId'])
        print("Image: " + instance['ImageId'])
