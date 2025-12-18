# rules.py
import re

def check_suspicious_words(job_description):
    suspicious_keywords = ['urgent', 'wire transfer', 'crypto wallet', 'pay first']
    for word in suspicious_keywords:
        if word.lower() in job_description.lower():
            return True
    return False

def check_salary(job_salary):
    # Example: Flag if salary is ridiculously high
    if job_salary and job_salary > 1000000:
        return True
    return False

def check_email(email):
    # Simple check for free email providers
    if email and re.search(r'@(gmail|yahoo|hotmail)\.com', email):
        return True
    return False

def check_missing_company(company_name):
    return not company_name or company_name.strip() == ""