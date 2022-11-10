from os import environ

import boto3


class S3:
    def __init__(self) -> None:
        self.client = boto3.client('s3')
        self.bucket_name = environ.get('BUCKET_NAME')

    def upload(self, upload_file, year, type):
        self.client.upload_fileobj(
            upload_file.file,
            self.bucket_name,
            f'{year}_{type}.pdf',
        )

    def download(self, year, type):
        self.client.download_file(
            self.bucket_name, f'{year}_{type}.pdf', f'/tmp/{year}_{type}.pdf'
        )
        return f'/tmp/{year}_{type}.pdf'

    def list(self):
        return [
            file['Key']
            for file in self.client.list_objects(Bucket=self.bucket_name)[
                'Contents'
            ]
        ]
