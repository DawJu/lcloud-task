import re
from s3 import s3_client, bucket_name, bucket_prefix

def list_all_files():
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=bucket_prefix)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print('Found no files.')

def upload_file(local_file_path, s3_file_name):
    try:
        s3_client.upload_file(local_file_path, bucket_name, f'{bucket_prefix}/{s3_file_name}')
        print(f'File {local_file_path} uploaded to {bucket_prefix}/{s3_file_name}')
    except Exception as e:
        print(f'Error uploading file: {e}')

def filter_files(filter):
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=bucket_prefix)
    if 'Contents' in response:
        regex = re.compile(filter)
        for obj in response['Contents']:
            if regex.search(obj['Key']):
                print(obj['Key'])
    else:
        print('Found no files.')

def filter_delete_files(filter):
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=bucket_prefix)
    if 'Contents' in response:
        regex = re.compile(filter)
        keys_to_delete = [{'Key': obj['Key']} for obj in response['Contents'] if regex.search(obj['Key'])]

        if keys_to_delete:
            delete_response = s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': keys_to_delete})
            print(f'Deleted files: {delete_response.get('Deleted', [])}')
        else:
            print('No files deleted.')
    else:
        print('Found no files.')
