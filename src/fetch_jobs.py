# fetch_jobs.py

def fetch_jobs():
    # Offline dummy job listings
    jobs = [
        {
            "title": "Software Engineer",
            "description": "Work on crypto projects. Urgent hiring!",
            "salary": 500000,
            "contact_email": "test@gmail.com",
            "company_name": "CryptoTech"
        },
        {
            "title": "Frontend Developer",
            "description": "Normal job, standard requirements.",
            "salary": 300000,
            "contact_email": "dev@company.com",
            "company_name": "WebCorp"
        },
        {
            "title": "Scam Job",
            "description": "Pay first, wire transfer required",
            "salary": 2000000,
            "contact_email": "fake@hotmail.com",
            "company_name": ""
        }
    ]
    return jobs
