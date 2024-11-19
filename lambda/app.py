import boto3
import json
import uuid
from datetime import datetime
import os

s3_client = boto3.client('s3')
dynamodb_client = boto3.resource('dynamodb')

S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
DYNAMODB_TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME')

def lambda_handler(event, context):
    try:
        file_content = event['fileContent']
        file_name = event['fileName']
        file_key = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        s3_key = f"{file_key}/{file_name}"
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=file_content
        )
        s3_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

        table = dynamodb_client.Table(DYNAMODB_TABLE_NAME)
        table.put_item(Item={
            'filekey': file_key,
            'FileName': file_name,
            'S3URL': s3_url,
            'Timestamp': timestamp
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded and metadata stored successfully.',
                'FileKey': file_key,
                'S3URL': s3_url
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred.',
                'error': str(e)
            })
        }
