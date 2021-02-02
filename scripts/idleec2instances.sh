#¡/bin/sh +x
echo "Fetch ec2 instances"

ec2_instance_ids=$(aws ec2 describe-instances --query 'Reservations[*].Instances[*].InstanceId' --output -text)
for ec2_instance_id in $ec2_instance_ids; do
end_date=$(date -d '1 week ago' --utc +%FT%TZ)
start_date=$(date -d '2 hour ago' --utc +%FT%TZ)

echo $ec2_instance_id

cpu_utilization=$(aws cloudwatch get-metric-statistics --metric-name CPUUtilization --namespace AWS/EC2 --start-time $start_date --end-time $end_date --period 3600 --statistics "Maximum" --dimensions Name=InstanceId,Value=$ec2_instance_id --query "Datapoints[0].Maximum")

echo $cpu_utilization

NetworkIn=$(aws cloudwatch get-metric-statistics --metric-name NetworkIn --namespace AWS/EC2 --start-time $start_date --end-time $end_date --period 3600 --statistics "Maximum" --dimensions Name=InstanceId,Value=$ec2_instance_id --query "Datapoints[0].Maximum")

echo $NetworkIn

if [ "$cpu_utilization" <= "0" && "$NetworkIn" <= "0"]; then
  echo $ec2_instance_id "is running idle"
fi
done
