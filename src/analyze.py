# analyze.py
from src.rules import (
    check_suspicious_words,
    check_salary,
    check_email,
    check_missing_company
)

def analyze_job(job):
    alerts = []
    risk_score = 0
    explanations = []

    # Rule 1: Suspicious language
    if check_suspicious_words(job.get("description", "")):
        alerts.append("Suspicious words detected")
        risk_score += 30
        explanations.append("Job description contains scam-related keywords")

    # Rule 2: Unrealistic salary
    if check_salary(job.get("salary", 0)):
        alerts.append("Unrealistic salary")
        risk_score += 25
        explanations.append("Salary is unusually high for the role")

    # Rule 3: Free email provider
    if check_email(job.get("contact_email", "")):
        alerts.append("Free email provider detected")
        risk_score += 20
        explanations.append("Recruiter is using a non-corporate email address")

    # Rule 4: Missing company name
    if check_missing_company(job.get("company_name", "")):
        alerts.append("Missing company name")
        risk_score += 25
        explanations.append("Company identity is not provided")

    # Risk classification
    if risk_score >= 80:
        risk_level = "High"
        status = "Scam"
    elif risk_score >= 50:
        risk_level = "Medium"
        status = "Unsafe"
    else:
        risk_level = "Low"
        status = "Safe"

    return {
        "title": job.get("title", "Unknown"),
        "company_name": job.get("company_name", "Unknown"),
        "description": job.get("description", ""),
        "salary": job.get("salary", 0),
        "contact_email": job.get("contact_email", ""),
        "alerts": alerts,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "explanations": explanations,
        "status": status
    }
