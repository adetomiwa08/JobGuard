JobGuard 🛡️
Job Scam Detection API powered by x402
JobGuard is a lightweight, rule-based job posting analysis service that helps job seekers identify potentially fraudulent or unsafe job listings before engaging with them. It analyzes job descriptions for common scam indicators and returns a structured risk assessment.
Built for the x402Jobs Hackathon, JobGuard integrates the x402 protocol to expose a paid, programmable API endpoint for job safety analysis.

🚨 Problem
Online job scams are increasingly common, especially in remote and Web3 job spaces. Many job seekers struggle to distinguish legitimate opportunities from scams that:
Request upfront payments
Use suspicious language
Avoid verifiable company details
Promise unrealistic rewards
JobGuard addresses this problem by providing instant, automated scam risk analysis for job postings.

✅ Solution
JobGuard exposes an API endpoint that:
Accepts a job description (text)
Runs it through predefined scam-detection rules
Returns:
A risk score
Scam indicators found
A safety verdict
The API is monetized and protected using x402, enabling trustless access control.

🧠 How It Works (Rule-Based Engine)
JobGuard analyzes job postings using heuristic rules such as:
Presence of upfront payment requests
Use of urgency or pressure language
Mentions of unrealistic salaries
Requests for private or unverifiable contact methods
Missing or vague company details
Each rule contributes to a cumulative risk score.

🏗️ Architecture
Client (Postman / Frontend)
        |
        v
   JobGuard API (FastAPI)
        |
        v
 Rule-Based Analyzer
        |
        v
 Scam Risk Response (JSON)

x402 handles:
API access control
Payment verification
Resource pricing

🔌 API Endpoint
POST /scan
Analyze a job posting for scam risk.
Request Body
'''
{
  "job_description": "We are hiring. Pay ₦5000 to get started..."
}
Response
Json
{
  "risk_score": 0.85,
  "verdict": "High Risk",
  "flags": [
    "Upfront payment request",
    "Urgent language detected"
  ]
}

🔐 x402 Integration
JobGuard uses x402 to:
Declare paid resources
Enforce access using the exact payment scheme
Enable programmable job-safety APIs

Example x402 discovery response:
Json
{
  "x402Version": 1,
  "accepts": [
    {
      "scheme": "exact",
      "network": "base",
      "maxAmountRequired": "0",
      "resource": "/scan",
      "description": "Analyze job postings for scam risk and safety"
    }
  ]
}

🛠️ Tech Stack
Python
FastAPI
x402
Postman (testing)
Rule-based NLP heuristics

🚀 Getting Started
1. Clone the Repository

Bash
git clone https://github.com/your-username/jobguard.git
cd jobguard

2. Install Dependencies

Bash
pip install -r requirements.txt

3. Run the Server

Bash
uvicorn main:app --reload

4. Test with Postman
Send a POST request to:

http://localhost:8000/scan

🎯 Hackathon Context
This project was built for the x402Jobs Hackathon to demonstrate:
A real-world problem
Practical x402 usage
A monetizable, developer-friendly API

🔮 Future Improvements
ML-based scam classification
Job URL and domain verification
Company reputation lookup
Browser extension for real-time scanning
Frontend dashboard for users

👤 Author
Tomiwa
Blockchain & Backend Developer
x402Jobs Hackathon Participant