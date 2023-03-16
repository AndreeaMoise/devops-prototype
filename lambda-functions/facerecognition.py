import boto3
import io
import base64
import json

from PIL import Image


rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

def lambda_handler(event, context):
    rawImage = event["image"]
    
    image = Image.open(io.BytesIO(base64.b64decode(rawImage)))
    
    stream = io.BytesIO()
    image.save(stream,format="JPEG")
    image_binary = stream.getvalue()
    
    
    response = rekognition.search_faces_by_image(
            CollectionId='deliverypersonnel',
            Image={'Bytes':image_binary}                                       
            )
    
    for match in response['FaceMatches']:
        print (match['Face']['FaceId'],match['Face']['Confidence'])
            
        face = dynamodb.get_item(
            TableName='facerecognition',  
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
            )
        
        if 'Item' in face:
            return {
                'statusCode': 200,
                'body': json.dumps(face['Item']['UserId']['S'])
            }
           
    return {
        'statusCode': 404,
        'body': json.dumps('Person cannot be recognized!')
    }

