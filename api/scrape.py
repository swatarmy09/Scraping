def handler(request):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"success": true, "count": 5, "message": "Scraper working"}'
    }