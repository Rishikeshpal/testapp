#!/usr/bin/env python

import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')
ec2_client=session.client('ec2',region_name='us-east-1')

details_volume_ids=[]

#list all ebs volume id & state.
#apply boto3 filter to only list available/unused volumes
#filsta={'Name':'staus','value':['available']}
#for volume in ec2.volumes.filter(filter=[filsta]):
#filter if volume has tags
#    print volume.id, volume.state, volume.tags
#you can use your own filter as well;use below

for volume in ec2.volumes.all():
    if volume.state=="available" and volume.tags==None:
        print volume.id, volume.state, volume.tags
        details_volume_ids.append(volume.id)

#delete volumes:

for volume in details_volume_ids:
    volume_tag=ec2.Volume(volume)
#    print dir(volume_tag)
    print "Deleting volume Id", volume
    volume_tag.delete()

#using ec2 waiter to finish volume deletion
waiter = ec2_client.get_waiter('volume_deleted')
try:
    waiter.wait(VolumeIds=details_volume_ids)
    print "successfully deleted all unused and untagged volumes"
except Exception as e:
    print e
