import boto3
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client('s3')
bucket_name = 'developer-task2'
bucket_prefix = 'TIE-rp'
