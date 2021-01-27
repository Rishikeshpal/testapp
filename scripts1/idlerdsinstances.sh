#¡/bin/sh +x
echo "Fetch RDS instances"

rds_instance_ids=$(aws rds describe-db-instances --query 'DBInstances[*].DBInstanceIdentifier' --output -text)
for rds_instance_id in $rds_instance_ids; do
end_date=$(date -d '2 hour ago' --utc +%FT%TZ)
start_date=$(date -d '2 hour ago 1 minute ago' --utc +%FT%TZ)

echo $rds_instance_id

number_connections=$(aws cloudwatch get-metric-statistics --metric-name DatabaseConnections --namespace AWS/RDS --start-time $start_date --end-time $end_date --period 3600 --statistics "Maximum" --dimensions Name=DBInstanceIdentifier,Value=$rds_instance_id --query "Datapoints[0].Maximum")

echo $number_connections

if [ "$number_connections" = "0.0"]; then
  echo $rds_instance_id "has zero connections"
fi
done
