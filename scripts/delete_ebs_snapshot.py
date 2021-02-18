#!/usr/bin/env python

from dattime import datetime, timezone, timedelta

import boto3
ec2 = boto3.resource('ec2')


#list ec2 snapshot based on OwnerIds
snapshots = ec2.snapshots.filter(OwnerIds=['jenbkins'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=xx)
    if delete_time > start_time:
        print('fmt_start_time = {}' And delete_time= {} '.format(start_time,delete_time))
        snapshot.delete()
        print('Snapshot Id: = {} is deleted'.format(snapshot.snapshot_id))
