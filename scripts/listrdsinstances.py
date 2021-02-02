import boto3

client = boto3.client('rds')

dbinstances = client.describe_db_instances()

all_list = dbinstances['DBInstances']

print('RDS Instance Name \t| Instance Type \t| Status')

for i in dbinstances['DBInstances']:
    dbInstanceName = i['DBInstanceIdentifier']
    dbInstanceEngine = i['DBInstanceClass']
    dbInstanceStatus = i['DBInstanceStatus']
    print('%s \t| %s \t| %s' %(dbInstanceName, dbInstanceEngine, dbInstanceStatus))
    
