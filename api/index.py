import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "PM Internship Scraper API",
            "version": "1.0",
            "project": "financialinsighthub-b6a2e",
            "endpoints": {
                "/api/scrape": "Scrape and save internships"
            }
        })
    }