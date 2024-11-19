# AWS Lambda S3 & DynamoDB Integration

This project contains an AWS Lambda function that uploads files to an S3 bucket and stores metadata in a DynamoDB table.

## Features
- Uploads file content to an S3 bucket.
- Stores file metadata (key, name, URL, timestamp) in DynamoDB.
- Includes a test event for validation.

## Setup Instructions

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Deploy using AWS SAM or CloudFormation:
    ```bash
    sam deploy --guided
    ```

3. Test the Lambda function with `test_event.json`.

## Environment Variables
- `S3_BUCKET_NAME`: Your S3 bucket name.
- `DYNAMODB_TABLE_NAME`: Your DynamoDB table name.

## Testing
Run a test event with:
```bash
sam local invoke "LambdaFunction" -e lambda/tests/test_event.json
