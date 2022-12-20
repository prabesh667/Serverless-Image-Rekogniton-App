from decimal import Decimal
import os
import boto3

dynamodb = boto3.resource("dynamodb")
labels_table = dynamodb.Table(os.environ.get("LABELS_TABLE", None))

def lambda_handler(event, context):

    rekognition_client = boto3.client('rekognition')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        response = rekognition_client.detect_labels(
            Image={"S3Object": {"Bucket": bucket,"Name": key},},
            MaxLabels=5,
            MinConfidence=70,)

        labels = response.get('Labels', None)

        for label in labels:
            labels_table.put_item(Item={
                "image-key": key,
                "image-label": label['Name'],
                "confidence": Decimal(label['Confidence'])
            })


