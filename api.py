# api.py
from fastapi import FastAPI, Request, HTTPException
from src.analyze import analyze_job
from x402 import x402_response  # your 402 response helper

app = FastAPI(
    title="JobGuard Scanner",
    description="Rule-based job scam detection engine",
    version="1.0.0"
)

@app.api_route("/scan", methods=["POST", "GET"])
async def scan_job(request: Request):
    """
    x402 callable job:
    - Responds 402 Payment Required if x402-payment header missing
    - Accepts POST requests with job JSON
    """
    # 1️⃣ Respond with 402 if payment header missing
    if request.headers.get("x402-payment") is None:
        return x402_response()  # returns 402 Payment Required JSON

    # 2️⃣ Ensure only POST processes job data
    if request.method != "POST":
        raise HTTPException(status_code=405, detail="Method Not Allowed")

    # 3️⃣ Parse job JSON and run JobGuard analysis
    job = await request.json()
    return analyze_job(job)

