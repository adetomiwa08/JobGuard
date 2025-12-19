from fastapi import FastAPI, Request, HTTPException
from src.analyze import analyze_job
from x402 import x402_response  # returns JSON with 402 Payment Required

app = FastAPI(
    title="JobGuard Scanner",
    description="Rule-based job scam detection engine",
    version="1.0.0"
)

@app.api_route("/scan", methods=["POST", "GET"])
async def scan_job(request: Request):
    # 1️⃣ Respond with 402 if x402-payment header missing
    if request.headers.get("x402-payment") is None:
        return x402_response()

    # 2️⃣ Only POST processes job data
    if request.method != "POST":
        raise HTTPException(status_code=405, detail="Method Not Allowed")

    job = await request.json()
    return analyze_job(job)
