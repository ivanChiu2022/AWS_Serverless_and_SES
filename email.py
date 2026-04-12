import json
import boto3

ses = boto3.client("ses", region_name="ca-central-1")  # use your SES region, e.g."us-east-1"

SENDER = "your-verified-sender@example.com"   # must be verified in SES
RECEIVER = "ylchiu1303@gmail.com"              # where you want to receive the message

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        user_email = body.get("email", "").strip()
        subject = body.get("subject", "").strip()
        message = body.get("message", "").strip()

        if not user_email or not subject or not message:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": json.dumps({"error": "email, subject, and message are required"})
            }

        email_body = f"""
New message from website contact form

From user: {user_email}
Subject: {subject}

Message:
{message}
"""

        response = ses.send_email(
            Source=SENDER,
            Destination={"ToAddresses": [RECEIVER]},
            Message={
                "Subject": {"Data": f"Website Contact: {subject}"},
                "Body": {
                    "Text": {"Data": email_body}
                }
            },
            ReplyToAddresses=[user_email]
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "message": "Email sent successfully",
                "messageId": response["MessageId"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"error": str(e)})
        }


        
