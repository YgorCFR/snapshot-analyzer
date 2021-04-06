import boto3
import click

@click.command()
@click.option('--profile', help="Name of the profile", required=True)
@click.option('--region', help="Name of the used AWS region", required=True)
def main(profile=None, region=None):
    # Starting session
    session = boto3.Session(profile_name=profile, region_name=region)
    # Attaching to EC2
    ec2 = session.resource('ec2')
    # Lising the instances
    for i in ec2.instances.all():
        print(f'INSTANCE OF ID: {i.id}')

if __name__ == '__main__':
    main()