import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test-site')
    
    update = table.update_item(
        Key={
            'counter': 'visitor',
            'type': '1'
        },
        UpdateExpression="set numCount = numCount + :inc",
        ExpressionAttributeValues={":inc": 1},
        ReturnValues="UPDATED_NEW"
    )
    
    update = update['Attributes']['numCount']

    return update