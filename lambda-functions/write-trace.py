import json
import boto3
import uuid

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        trace = dynamodb.put_item(
            TableName='traces',  
            Item={
                'id': {
                  'S': str(uuid.uuid1())
                },
                'trace': {
                    'S': event['driverId']
                },
                'truckId': {
                    'S': event['truckId']
                },
                'location': {
                    'S': json.dumps(event['location'])
                },
                'load': {
                    'S': json.dumps(event['load'])
                },
            }
        )
    except Exception as e:
        print("An exception occurred", e)
        return {
            'statusCode': 400,
            'body': json.dumps('Cannot add trace')
        }  
            
    return {
        'statusCode': 200
    }
