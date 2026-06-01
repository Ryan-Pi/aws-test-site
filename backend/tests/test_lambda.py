import sys
import boto3
from moto import mock_dynamodb
import unittest
sys.path.append('backend/code')
from get_visitors import lambda_handler

class TestAPI(unittest.TestCase):
    @mock_dynamodb
    def setUp(self) -> None:
        dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-2")
        dynamodb.create_table(
            TableName = "test-site",
            KeySchema = [{"AttributeName": "counter", "KeyType": "HASH"}],
        AttributeDefinitions=[
            {
                "AttributeName": "counter",
                "AttributeType": "S",
            },
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
        
    @mock_dynamodb
    def test_fetch_count_works(self):
        result = lambda_handler(0,0)
        self.assertEqual(result['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()





