import os
import json
import time
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase only once
def init_firebase():
    if not firebase_admin._apps:
        firebase_config = {
            "type": "service_account",
            "project_id": "financialinsighthub-b6a2e",
            "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.environ.get('FIREBASE_CLIENT_EMAIL')}"
        }
        cred = credentials.Certificate(firebase_config)
        firebase_admin.initialize_app(cred, {
            "projectId": "financialinsighthub-b6a2e",
            "databaseURL": "https://financialinsighthub-b6a2e-default-rtdb.firebaseio.com",
            "storageBucket": "financialinsighthub-b6a2e.firebasestorage.app"
        })
    return firestore.client()

# Scraper function
def scrape_internships():
    response = requests.get(
        "https://pminternship.mca.gov.in/internships",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(response.content, "html.parser")

    internships = []
    cards = soup.find_all(["div", "article"], class_=lambda x: x and any(
        keyword in x.lower() for keyword in ["internship", "job", "card", "listing"]
    ))

    for card in cards[:10]:
        title_elem = card.find(["h1", "h2", "h3", "h4"], string=lambda x: x and len(x.strip()) > 5)
        title = title_elem.get_text().strip() if title_elem else "PM Internship"

        internships.append({
            "title": title,
            "organization": "Government of India",
            "description": "Government internship program",
            "location": "New Delhi",
            "skillsRequired": "Government,Policy,Administration",
            "duration": "3 months",
            "stipend": "₹10,000",
            "imageUrl": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
            "companyLogo": "https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg",
            "timestamp": int(time.time() * 1000)
        })
    return internships

# Vercel entrypoint
def handler(request):
    try:
        db = init_firebase()
        internships = scrape_internships()

        if internships:
            batch = db.batch()
            for internship in internships:
                doc_ref = db.collection("internships").document()
                batch.set(doc_ref, internship)
            batch.commit()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"success": True, "count": len(internships)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"success": False, "error": str(e)})
        }
