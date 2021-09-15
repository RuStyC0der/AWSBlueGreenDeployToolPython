from icecream import ic


def get_instance_by_name(InstanceName, ec2_client):

    '''returns first instance with @InstanceName in tag Name'''

    response = ec2_client.describe_instances(Filters=[
        {
            'Name': 'tag:Name',
            'Values': [InstanceName]
        }
    ]
    )

    return response['Reservations'][0]['Instances'][0]

def get_instance_by_id(InstanceId, ec2_client):

    '''returns first instance with @InstanceId in tag Name'''

    response = ec2_client.describe_instances(InstanceIds=[InstanceId])

    return response['Reservations'][0]['Instances'][0]

def create_instance():
    pass

def duplicate_instance_with_another_os():
    pass

def duplicate_instance(instance, ec2_client):
    
    Placement = instance['Placement']
    BlockDeviceMappings_raw = instance['BlockDeviceMappings']

    # extract device names and volume id`s to snapshot generate
    BlockDeviceMappings_with_volume_id = list(map( lambda x: {'DeviceName':x['DeviceName'], 'VolumeId':x['Ebs']['VolumeId']}, BlockDeviceMappings_raw))
    
    ic(Placement)
    ic(BlockDeviceMappings_with_volume_id)
    

