import argparse
from functions import list_all_files, upload_file, filter_files, filter_delete_files

def main():

    parser = argparse.ArgumentParser(description='S3 bucket CLI')
    parser.add_argument('--list', action='store_true', help='List all files in the bucket')
    parser.add_argument('--upload', nargs=2, metavar=('local_file', 'bucket_location'), help='Upload a file to the bucket')
    parser.add_argument('--filter', metavar='regex', help='List all files in the bucket that match the filter regex')
    parser.add_argument('--delete', metavar='regex', help='Delete all files in the bucket that match the filter regex')

    args = parser.parse_args()

    if args.list:
        list_all_files()
    elif args.upload:
        upload_file(args.upload[0], args.upload[1])
    elif args.filter:
        filter_files(args.filter[0])
    elif args.delete:
        filter_delete_files(args.delete[0])

if __name__ == "__main__":
    main()
