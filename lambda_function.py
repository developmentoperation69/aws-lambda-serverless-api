import json

def lambda_handler(event, context):
    response = {
        "message": "Hello from AWS Lambda!",
        "name": "Usama",
        "service": "Serverless API",
        "status": "Success"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
