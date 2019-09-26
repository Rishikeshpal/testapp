#¡/bin/sh +x
echo "Fetch ebs volumes"

ebs_volumes=$(aws ec2 describe-volumes --query 'Volumes[].Attachments[?(Device!=`/dev/xvda`) && (Device!=`/dev/sda1`)].VolumeId | []' --output -text)
for ebs_volume in $ebs_volumes; do
end_date=$(date -d '1 week ago' --utc +%FT%TZ)
start_date=$(date -d '2 hour ago' --utc +%FT%TZ)

echo $ebs_volume

readops=$(aws cloudwatch get-metric-statistics --metric-name VolumeReadOps --namespace AWS/EBS --start-time $start_date --end-time $end_date --period 3600 --statistics "Sum" --dimensions Name=VolumeId,Value=$ebs_volume --query "Datapoints[0].Sum")

echo $readops

writeops=$(aws cloudwatch get-metric-statistics --metric-name VolumeWriteOps --namespace AWS/EBS --start-time $start_date --end-time $end_date --period 3600 --statistics "Sum" --dimensions Name=VolumeId,Value=$ebs_volume --query "Datapoints[0].Sum")

echo $writeops
if [ "$readops"  = "0.0" && "$writeops" = "0.0" ]; then
  echo $ebs_volume "is running idle"
fi
done
