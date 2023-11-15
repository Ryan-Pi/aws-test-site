import json
import boto3

def lambda_handler(event, context):
    # define dynamodb resources
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test-site')
    
    # increment visitor count by 1 and then return visitor count
    update = table.update_item(
        Key={
            'counter': 'visitor',
            'type': '1'
        },
        UpdateExpression="set numCount = numCount + :inc",
        ExpressionAttributeValues={":inc": 1},
        ReturnValues="UPDATED_NEW"
    )
    
    # extract visitor count from json response and return to requester
    update = update['Attributes']['numCount']

    return update