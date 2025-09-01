from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "PM Internship Scraper API",
        "version": "1.0",
        "project": "financialinsighthub-b6a2e",
        "endpoints": {
            "/api/scrape": "Scrape and save internships"
        }
    })

if __name__ == '__main__':
    app.run()