import json
import boto3

#create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('TextractDatabase')
def lambda_handler(event, context):
    response = table.get_item(
        TableName='TextractDatabase',
        Key={
            'ID': "2"
        },
        AttributesToGet=['Full Name:','Phone Number:','Mailing Address:','Home Address:',],
    )
    ans = str(response)
    response = ans.split(',', 6)[0]+ans.split(',', 6)[1]+ans.split(',', 6)[2]+ans.split(',',6 )[3]+ans.split(',',6 )[4]+ans.split(',',6 )[5]
    
    return {
        'statusCode': 200,
        'body': str(response)
    }
