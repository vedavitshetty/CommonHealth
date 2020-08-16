import json
import boto3
from trpp import Document
from time import gmtime, strftime

#create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('TextractDatabase')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    # Document
    s3BucketName = "keerthmedhacks"
    documentName = "employmentapp.png"
    
    # Amazon Textract client
    textract = boto3.client('textract')
    
    # Call Amazon Textract
    response = textract.analyze_document(
        Document={
            'S3Object': {
                'Bucket': "keerthmedhacks",
                'Name': "employmentapp.png"
            }
        },
        FeatureTypes=["FORMS"])
    
    #print(response)
    
    doc = Document(response)
    keys = []
    values =[]
    for page in doc.pages:
        # Print fields
        print("Fields:")
        for field in page.form.fields:
            #print("Key: {}, Value: {}".format(field.key, field.value))
            keys.append(str(field.key))
            values.append(str(field.value))
        
        response = table.put_item(
            Item={
                'ID' : "2",
                keys[0] : values[0],
                keys[1] : values[1],
                keys[2] : values[2],
                keys[3] : values[3],
                'Time Recorded' : now
            })
        
    response = table.get_item(
        TableName='TextractDatabase',
        Key={
            'ID': "2"
        })
    
    return {
        'statusCode' : 200,
        'body':json.dumps(response)
    }
        