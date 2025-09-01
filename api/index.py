import os
import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "has_private_key": bool(os.environ.get("FIREBASE_PRIVATE_KEY")),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
            "project_id": os.environ.get("FIREBASE_PROJECT_ID", "not set")
        })
    }
