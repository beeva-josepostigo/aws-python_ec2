import boto3
from ejemplo.ec2Credentials import openSession

#Return list with names of instances 
def get_instances():
    instances=list()
    client = openSession().client('ec2')
    ec2=client.describe_instances()

    for i in ec2['Reservations']:
        for x in i['Instances']:
            for s in x['Tags']:
                if s['Key'] == "Name":
                    instances.append(s['Value'])
    return instances

#Return list with volumeId's of instances
def get_volumes():
    volumes=list()
    client = openSession().client('ec2')
    ec2=client.describe_volumes()

    for i in ec2['Volumes']:
        for x in i['Attachments']:
            volumes.append(x['InstanceId'])

    return volumes

#Return list with VpcId's of instances
def get_vpcs():
    vpcs = list()
    client = openSession().client('ec2')
    ec2 = client.describe_vpcs()

    for i in ec2['Vpcs']:
        vpcs.append(i['VpcId'])

    return vpcs

#Return instance ID of a instance whose name is 'AlphaGroup'
def get_instanceIdfromName():

    client = openSession().client('ec2')
    ec2 = client.describe_instances(
        Filters=[
            {
                'Name':'tag-value',
                'Values':['AlphaGroup']
            }
        ])

    for i in ec2['Reservations']:
        for x in i['Instances']:
            instanceId=x['InstanceId']

    return instanceId

#Put a 'Name' tag in a instance with value 'value'
def put_tagInInstance(value):

    client = openSession().resource('ec2')
    client.create_tags(Resources=[get_instanceIdfromName()],Tags=[
        {
            'Key':'Name',
            'Value':value
        }])

#Launch a instance with features indicated
def launch_instance():
    client = openSession().client('ec2')
    instances = client.run_instances(ImageId='ami-9398d3e0',MinCount=1,MaxCount=1,KeyName='alpha',
                                     InstanceType='t2.micro',Monitoring={'Enabled':False},
                                     NetworkInterfaces=[{'DeviceIndex':0,'AssociatePublicIpAddress':True,
                                                         'SubnetId':'subnet-f1e770a9'}])
