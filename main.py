import argparse
from functions import list_all_files, upload_file

def main():

    parser = argparse.ArgumentParser(description='S3 bucket CLI')
    parser.add_argument('--list', action='store_true', help='List all files in the bucket')
    parser.add_argument('--upload', nargs=2, metavar=('local_file', 'bucket_location'), help='Upload a file to the bucket')

    args = parser.parse_args()

    if args.list:
        list_all_files()
    elif args.upload:
        upload_file(args.upload[0], args.upload[1])

if __name__ == "__main__":
    main()
