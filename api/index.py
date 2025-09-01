def handler(request):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"status": "PM Internship Scraper API", "version": "1.0"}'
    }