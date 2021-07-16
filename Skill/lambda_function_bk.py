"""
import json
import boto3


def lambda_handler(event, context):
    print(f"event:{event}")
    topic = 'test/pub'
    payload = "Forward"
    
    try:
        iot = boto3.client('iot-data', endpoint_url="a1g1dkjw8ju89u-ats.iot.ap-northeast-1.amazonaws.com")
        iot.publish(
            topic=topic,
            qos=0,
            payload=json.dumps(payload, ensure_ascii=False)
        )
 
        return "Succeeeded."
    
    except Exception as e:
        print(e)
        return "Failed."
"""