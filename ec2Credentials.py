import boto3
import yaml

#Function to open boto3 session (connection with AWS) using credentials saved in a file indicated as parameter 
def openSession():
    with open("/home/josepostigo/amazon/ejemplo/config/credential.yaml","r") as credential_file:

        credentials=yaml.load(credential_file)

        session=boto3.Session(aws_access_key_id=credentials['config']['aws_access'],
                       aws_secret_access_key=credentials['config']['aws_secret'])

    return session

