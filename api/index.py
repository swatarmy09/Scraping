def handler(request):
    try:
        # Debug environment
        debug = {
            "has_private_key": bool(os.environ.get("FIREBASE_PRIVATE_KEY")),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID")
        }
        print("DEBUG ENV:", debug)
