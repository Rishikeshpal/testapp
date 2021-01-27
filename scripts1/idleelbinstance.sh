#¡/bin/sh +x
echo "Fetch elbs"

elb_instances=$(aws ec2 describe-load-balancers --query 'LoadBalancerDescriptions[*].LoadBalancerName' --output -text)
for elb_instance in $elb_instances; do
end_date=$(date -d '1 week ago' --utc +%FT%TZ)
start_date=$(date -d '2 hour ago' --utc +%FT%TZ)

echo $elb_instance

request_count=$(aws cloudwatch get-metric-statistics --metric-name RequestCount --namespace AWS/EC2 --start-time $start_date --end-time $end_date --period 3600 --statistics "Sum" --dimensions Name=LoadBalancerName,Value=$elb_instance --query "Datapoints[0].Sum")

echo $request_count


if [ "$request_count"  = "0.0" ]; then
  echo $elb_instance "is running idle"
fi
done
