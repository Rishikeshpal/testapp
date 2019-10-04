#!/usr/bin/env python
#list amis older than xx days

from dattime import datetime, timezone, timedelta

import boto3
ec2 = boto3.resource('ec2')


#list amis based on OwnerIds
amilist = ec2.images.filter(OwnerIds=['jenbkins'])

for ami in amilist:
    start_time = ami.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=xx)
    if delete_time > start_time:
        print('fmt_start_time = {}' And delete_time= {} '.format(start_time,delete_time))
        image.deregister()
        print('AMI: = {} is deregistered'.format(ami.image_id ))
