#¡/usr/bin/env python
#list unused elactic ips and release them if necessary
import boto3
client = boto3.client('ec2')

eips_list = client.describe_addresses()
for eip in eips_list['Addresses']:

#filter based on NetworkInterfaceIf or InstanceId:

    if "NetworkInterfaceId"  not in eip:
        print(eip['PublicIp'])
        #add these line if you want to release elastic ip.
        client.release_address(AllocationId=eip['AllocationId'])
        
