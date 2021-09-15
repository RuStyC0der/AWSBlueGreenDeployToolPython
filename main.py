import boto3
from icecream import ic

from ec2_utils.volume_utils import *
from ec2_utils.instance_utils import *
from ec2_utils.tag_utils import *

ec2 = boto3.client('ec2', region_name='us-west-2', aws_access_key_id='AKIAYLR57AQ3ANYDBQWE', aws_secret_access_key='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')

server = get_instance_by_name(InstanceName='server', ec2_client=ec2)

ic(server['InstanceId'])
# ic(server['Tags'])


# ic(get_tags(ResourceId=server['InstanceId'], ec2_client=ec2))

# create_tags(ResourceId='vol-0b564168daf6c9c99', tags=[{'Key': 'Name', 'Value': 'server_new'}], ec2_client=ec2)

def copy_volume(server, ec2):
    response = create_snapshot(
        VolumeId=server['BlockDeviceMappings'][0]['Ebs']['VolumeId'], ec2_client=ec2)

    SnapshotId = response['SnapshotId']
    AvailabilityZone = server['Placement']['AvailabilityZone']

    ic(create_volume(SnapshotId=SnapshotId,
       ec2_client=ec2, AvailabilityZone=AvailabilityZone))
    ic(delete_snapshot(SnapshotId=SnapshotId, ec2_client=ec2))


# copy_volume(server, ec2)
# delete_all_tags(ResourceId='vol-01a87681e4f05b2ad', ec2_client=ec2)

# transfer_tags(ResourceIdFrom='vol-0b564168daf6c9c99', ResourceIdTo='vol-01a87681e4f05b2ad', ec2_client=ec2, Strict=True)


# duplicate_instance(server, ec2)

# instances = ec2.run_instances(
#     MinCount=1,
#     MaxCount=1,
#     InstanceType='t2.micro',
#     KeyName='factorioServer',
#     ImageId='ami-03d5c68bab01f3496',
#     # BlockDeviceMappings=[
#     #     {
#     #         'DeviceName': '/dev/sda1',
#     #         'Ebs': {
#     #             'SnapshotId': 'snap-0c8a14d0442ddad3b',
#     #         }}]
# )


# ec2.create_image(InstanceId=instance_id, NoReboot=True, Name="abc")