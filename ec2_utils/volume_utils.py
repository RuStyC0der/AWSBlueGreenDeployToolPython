def create_snapshot(*,VolumeId, ec2_client):

    response = ec2_client.create_snapshot(VolumeId=VolumeId)

    snapshotId = response['SnapshotId']

    waiter = ec2_client.get_waiter('snapshot_completed')

    waiter.wait(SnapshotIds=[snapshotId])

    return response

def delete_snapshot(*, SnapshotId, ec2_client):

    return ec2_client.delete_snapshot(SnapshotId=SnapshotId)


def create_volume(*, Size=0, SnapshotId=None, AvailabilityZone, ec2_client):
    
    response = ec2_client.create_volume(Size=Size, SnapshotId=SnapshotId, AvailabilityZone=AvailabilityZone)

    waiter = ec2_client.get_waiter('volume_available')

    waiter.wait(VolumeIds=[response['VolumeId']])

    return response


