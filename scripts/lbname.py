#¡/uer/bin/env python
import boto3
#use elb as it will list classic loadbalanceres which has instances attached to it
lblist = boto3.client('elb')
ec2 = boto3.resource('ec2')

lbs = lblist.describe_load_balancers()
for elb in lbs['LoadBalancerDescriptions']:
    print('DNSName : ' + elb['LoadBalancerName'])
    for ins in elb['Instances']:
        running_instances = \
            ec2.instances.filter(Filters=[{'Name': 'instance-state-name'
                                 , 'Values': ['running']},
                                 {'Name': 'instance-id',
                                 'Values': [ins['InstanceId']]}])
        for instance in running_instances:
            print("Instance : " + instance.public_dns_name);
