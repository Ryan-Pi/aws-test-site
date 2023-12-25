import json
import boto3

def lambda_handler(event, context):
    # define dynamodb resources
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test-site')
    
    visitors = table.get_item(Key={
        'counter': 'visitor'
        }
    )
    
    # if visitor item is non-existent, create new item
    if "Item" not in visitors:
        table.put_item(
            Item={'counter': 'visitor','numCount': 1}
        )
        return 1
    else:
    # increment visitor count by 1 and then return visitor count
        update = table.update_item(
            Key={
                'counter': 'visitor'
            },
            UpdateExpression="set numCount = numCount + :inc",
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW"
        )
    
    # extract visitor count from json response and return to requester
    # could just return this instead, but leaving it in for now
    update = update['Attributes']['numCount']

    return respond(update)

def respond(visitCount):
    object = {"numVisitors": int(visitCount)}
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": object,
    }
    
    return json.dumps(response)