import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg', 'elonm', 'ce71c344-c3d2-11ed-afa1-0242ac120002'),
      ('image2.jpg', 'elonm', 'ce71c344-c3d2-11ed-afa1-0242ac120002'),
      ('image3.jpg', 'billg', 'eb118b1a-c3d2-11ed-afa1-0242ac120002'),
      ('image4.jpg','billg', 'eb118b1a-c3d2-11ed-afa1-0242ac120002'),
      ('image5.jpg', 'andreeam', 'f63c54f2-c3d2-11ed-afa1-0242ac120002'),
      ('image6.jpg', 'andreeam', 'f63c54f2-c3d2-11ed-afa1-0242ac120002'),
      ('image7.jpg', 'andreeam', 'f63c54f2-c3d2-11ed-afa1-0242ac120002')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('delivery-personnel-faceprints', image[0])
    ret = object.put(Body=file,
                    Metadata={'username':image[1], 'userid':image[2]})