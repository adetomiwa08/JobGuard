# JobGuard

**JobGuard** is a rule-based job scam detection engine built for the x402 Hackathon. It analyzes job postings for suspicious signs of scams, calculates a risk score, and provides actionable alerts. Exposed as a webhook via FastAPI, it’s ready for x402scan integration and pay-per-use registration.

---

## Features

- Detects suspicious language, unrealistic salaries, free email usage, and missing company info.
- Calculates risk score and classifies risk level: Low / Medium / High.
- Returns structured alerts and explanations for each job post.
- Exposed as `/scan` API endpoint for easy integration.

---

## Tech Stack

- Python 3.11+  
- FastAPI & Uvicorn  
- Rule-based detection logic  
- x402-ready webhook

---

## Quick Start

1. **Clone repository**
```bash
git clone https://github.com/adetomiwa08/JobGuard.git
cd JobGuard
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run API locally
```bash
python -m uvicorn api:app --reload
```
Swagger docs: http://127.0.0.1:8000/docs

4. Test /scan endpoint
   POST /scan
```bash
{
  "title": "Remote Data Entry",
  "company_name": "",
  "description": "No interview, fast money",
  "salary": 500000,
  "contact_email": "hiring@gmail.com"
}
```
Response includes: alerts, risk_score, risk_level, explanations, status.

Project Structure
```
JobGuard/
├── api.py          # FastAPI app
├── src/            # Core logic
│   ├── analyze.py
│   ├── fetch_jobs.py
│   ├── rules.py
│   ├── save.py
│   └── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

Hackathon Compliance

- Unique x402 resource: /scan API
- Registered and callable via webhook
- Structured input/output, pay-per-use ready

Author

Adetomiwa Adewale
GitHub: https://github.com/adetomiwa08



