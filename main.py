import boto3
import click
import logging

# Defining logging settings
logger = logging.getLogger()  # Set logger as a variable to be used
logging.basicConfig(format='[%(levelname)s][%(asctime)s]:%(message)s',level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')  # Limit logger for code 10 or higher


@click.command()
@click.option('--profile', help="Name of the profile", required=True)
@click.option('--region', help="Name of the used AWS region", required=True)
def main(profile=None, region=None):
    # Starting session
    session = boto3.Session(profile_name=profile, region_name=region)
    # Attaching to EC2
    ec2 = session.resource('ec2')
    # List instances
    logger.info(list_instances(ec2))
    
def list_instances(ec2):
    '''
        The function that list the instances
    '''
    # Listing the instances id's and other characteristics
    return [', '.join((instance.id, 
                      instance.instance_type,
                      instance.placement['AvailabilityZone'],
                      instance.state['Name'],
                      instance.public_dns_name)) for instance in ec2.instances.all()]

if __name__ == '__main__':
    main()