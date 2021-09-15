from icecream import ic
from botocore.exceptions import ClientError

def create_tags(*, ResourceId, Tags, ec2_client):

    try:
        ec2_client.create_tags(Resources=[ResourceId], Tags=Tags, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    return ec2_client.create_tags(Resources=[ResourceId], Tags=Tags)


def delete_tags(*, ResourceId, Tags, ec2_client):
    try:
        ec2_client.delete_tags(Resources=[ResourceId], Tags=Tags, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    return ec2_client.delete_tags(Resources=[ResourceId], Tags=Tags, DryRun=False)


def get_tags(*, ResourceId, ec2_client):
    response = ec2_client.describe_tags(
        DryRun=False,
        Filters=[
            {
                'Name': 'resource-id',
                'Values': [
                    ResourceId,
                ]
            },
        ],
    )

    raw_tags = response['Tags']

    # leave only tag keys and values (removing keys such as DeviceId etc.)
    tags = [{'Key': i['Key'], 'Value': i['Value']} for i in raw_tags]

    return tags

def delete_all_tags(*, ResourceId, ec2_client):

    tags = get_tags(ResourceId=ResourceId, ec2_client=ec2_client)
    return delete_tags(ResourceId=ResourceId, Tags=tags, ec2_client=ec2_client)



def transfer_tags(*, ResourceIdFrom, ResourceIdTo, ec2_client, Strict=False):

    tags = get_tags(ResourceId=ResourceIdFrom, ec2_client=ec2_client)
    ic(tags)

    if (Strict):
        delete_all_tags(ResourceId=ResourceIdTo, ec2_client=ec2_client)
    
    return create_tags(ResourceId=ResourceIdTo, Tags=tags, ec2_client=ec2_client)
