# snapshot-analyzer
A script that analyses the AWS EC2 instances and snapshots

## About

This project is a demo that uses boto3 to manage EC2 instance snapshots.

## Configuring

It uses configuration file created by AWS cli. e.g.:

`aws configure --profile <<YOUR_PROFILE_NAME>>`

Install the pipenv dependency

`pip install -r requirements.txt`


## Running

`pipenv run main.py --profile <<YOUR_PROFILE_NAME>> --region <<YOUR_REGION_NAME>>`