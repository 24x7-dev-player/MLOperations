import boto3

# Create a boto3 client for EC2 and Auto Scaling
ec2_client = boto3.client('ec2')
autoscaling_client = boto3.client('autoscaling')

# Create a launch template
response = ec2_client.create_launch_template(
    LaunchTemplateName='my-launch-template',
    VersionDescription='Initial version',
    LaunchTemplateData={
        'ImageId': 'ami-12345678',
        'InstanceType': 't2.micro',
        'KeyName': 'my-key-pair',
        'SecurityGroups': ['my-security-group'],
        # Add any other desired configurations
    }
)

# Get the ID of the created launch template
launch_template_id = response['LaunchTemplate']['LaunchTemplateId']

# Create an auto scaling group
response = autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    LaunchTemplate={
        'LaunchTemplateName': 'my-launch-template',
        'Version': '$Latest'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    VPCZoneIdentifier='subnet-12345678',  # Specify your subnet ID
    # Add any other desired configurations
)

# Attach a scaling policy
response = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='my-scaling-policy',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization',
        },
        'TargetValue': 60,
        'DisableScaleIn': False,
    }
)

# Get the ARN of the created scaling policy
scaling_policy_arn = response['PolicyARN']

print(f"Launch template ID: {launch_template_id}")
print(f"Auto Scaling Group created with policy ARN: {scaling_policy_arn}")
