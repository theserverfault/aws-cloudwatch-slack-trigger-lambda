from json import dumps, loads
import json
from os import environ
from sys import getsizeof

from requests import post

def generic_block_builder(message):
    tokens = message['AlarmName'].split('-')
    aws_service_name = tokens[0]
    metric = tokens[1]
    service = '-'.join(tokens[2:])
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Alert :alert:*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Environment*: {0}".format(environ['ENVIRONMENT'])
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Category*: {0}".format(aws_service_name)
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Identifier*: {0}".format(service)
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Alarm*: {0}".format(message['AlarmName'])
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Description*: {0}".format(message['AlarmDescription'])
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Reason*: {0}".format(message['NewStateReason'])
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "View Alarm in Console :aws:",
                            "emoji": True
                        },
                        "url": "https://console.aws.amazon.com/cloudwatch/home?region=ap-south-1#alarm:alarmFilter=ANY;name={0}".format(message['AlarmName'])
                    }
                ]
            }
        ]
    }

def trigger_slack_webhook(data, team_identifier):
    webhook_name = "{0}_webhook".format(team_identifier)
    slack_webhook = environ[webhook_name]
    byte_length = str(getsizeof(data))
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': byte_length
    }
    response = post(slack_webhook, data=dumps(data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    print('Sent trigger')
    return


def send_message(event):
    eventSubscriptionARN = event['Records'][0]['EventSubscriptionArn'].split(":")
    team_identifier = eventSubscriptionARN[5].split("-")[1]
    eventMessage = loads(event['Records'][0]['Sns']['Message'])
    payload = generic_block_builder(eventMessage)
    trigger_slack_webhook(payload, team_identifier)


def lambda_handler(event, context):
    print(event)
    send_message(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda')
    }
