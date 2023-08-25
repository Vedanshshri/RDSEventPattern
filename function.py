import boto3
import socket
def lambda_handler(event, context):
    # Retrieve the current IP address of the RDS instance
    rds_client = boto3.client('rds')
    response = rds_client.describe_db_instances(DBInstanceIdentifier='database-1')
    rds_ip = response['DBInstances'][0]['Endpoint']['Address']
    print(rds_ip)



    data = socket.gethostbyname_ex(rds_ip)
    print (data[-1][0])
    # Update the IP address of the NLB target
    nlb_client = boto3.client('elbv2')
    # Remove Unhealthy Targets
    health = nlb_client.describe_target_health(TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:723188152828:targetgroup/t3est/31516dbac3540756')
    print(health)
    health = health['TargetHealthDescriptions']
    targets = [x['Target'] for x in health if x['TargetHealth']['State'] == 'unhealthy' ]
    if targets:
        nlb_client.deregister_targets(TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:723188152828:targetgroup/t3est/31516dbac3540756' ,Targets=targets)
    response = nlb_client.register_targets(TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:723188152828:targetgroup/t3est/31516dbac3540756', Targets=[{'Id': data[-1][0], 'Port': 3306}])
    
    print('NLB target updated with RDS IP:', rds_ip)
