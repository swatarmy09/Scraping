# PM Internship Scraper - Vercel

## Structure
```
scraper/
├── api/
│   ├── index.py      # Main endpoint
│   └── scrape.py     # Scraping function
├── vercel.json       # Vercel config
├── requirements.txt  # Dependencies
└── README.md         # This file
```

## Vercel Deployment

### 1. Environment Variables
Add in Vercel dashboard:
```
FIREBASE_PRIVATE_KEY_ID=your_key_id
FIREBASE_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nyour_key\n-----END PRIVATE KEY-----
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@financialinsighthub-b6a2e.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=your_client_id
```

### 2. Deploy
```bash
npm i -g vercel
vercel --prod
```

## Endpoints
- `GET /` - API status
- `GET /api/scrape` - Scrape internships

## Firebase Project
- Project ID: `financialinsighthub-b6a2e`