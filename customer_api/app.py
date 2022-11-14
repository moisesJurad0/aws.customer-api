import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('CUSTOMERS_TABLE')
