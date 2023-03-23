import boto3
import io
import base64
from PIL import Image

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

image_path = "/9j/4AAQSkZJRgABAQEAeAB4AAD/4RD0RXhpZgAATU0AKgAAAAgABAE7AAIAAAAOAAAISodpAAQAAAABAAAIWJydAAEAAAAcAAAQ0OocAAcAAAgMAAAAPgAAAAAc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEFuZHJlZWEgTW9pc2UAAAWQAwACAAAAFAAAEKaQBAACAAAAFAAAELqSkQACAAAAAzkxAACSkgACAAAAAzkxAADqHAAHAAAIDAAACJoAAAAAHOoAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAyMDIzOjAzOjE2IDA5OjU5OjA2ADIwMjM6MDM6MTYgMDk6NTk6MDYAAABBAG4AZAByAGUAZQBhACAATQBvAGkAcwBlAAAA/+ELIGh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8APD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4NCjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iPjxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+PHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9InV1aWQ6ZmFmNWJkZDUtYmEzZC0xMWRhLWFkMzEtZDMzZDc1MTgyZjFiIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iLz48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyI+PHhtcDpDcmVhdGVEYXRlPjIwMjMtMDMtMTZUMDk6NTk6MDYuOTA3PC94bXA6Q3JlYXRlRGF0ZT48L3JkZjpEZXNjcmlwdGlvbj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+PGRjOmNyZWF0b3I+PHJkZjpTZXEgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOmxpPkFuZHJlZWEgTW9pc2U8L3JkZjpsaT48L3JkZjpTZXE+DQoJCQk8L2RjOmNyZWF0b3I+PC9yZGY6RGVzY3JpcHRpb24+PC9yZGY6UkRGPjwveDp4bXBtZXRhPg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8P3hwYWNr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"
image = Image.open(io.BytesIO(base64.b64decode(image_path)))
print(image)
stream = io.BytesIO()
image.save(stream,format="PNG")
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(
        CollectionId='deliverypersonnel',
        Image={'Bytes':image_binary}                                       
        )

found = False
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(
        TableName='facerecognition',  
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print ("Found Person: ",face['Item']['UserId']['S'], face['Item']['Username']['S'])
        found = True

if not found:
    print("Person cannot be recognized")