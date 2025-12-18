from fastapi import FastAPI
from src.analyze import analyze_job

app = FastAPI(
    title="JobGuard Scanner",
    description="Rule-based job scam detection engine",
    version="1.0.0"
)

@app.post("/scan")
def scan_job(job: dict):
    """
    x402 callable job:
    - Accepts job data
    - Runs JobGuard analysis
    - Returns risk assessment
    """
    return analyze_job(job)
