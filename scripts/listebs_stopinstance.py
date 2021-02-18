#!/usr/bin/python

import boto3

def main():
    ec2 = boto3.resource('ec2', region_name="us-west-2")
    client = boto3.client('ec2', region_name="us-west-2")
    volumes = ec2.volumes.all()

    for vol in volumes:

        for instance in vol.attachments:
            instances = instance.get('InstanceId')
            print(instances)
            for ins in instances:
                if ins.state["Name"] == "stopped":
                   print (ins.id) 
if __name__ == '__main__':
    main()
