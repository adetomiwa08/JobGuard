from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

JOBGUARD_URL = "https://jobguard.up.railway.app/scan"

@app.post("/scan")
async def scan_job(job: dict):
    # Always return 402 to satisfy x402scan webhook
    raise HTTPException(status_code=402, detail="Payment Required")
    # If you wanted, you could forward to JobGuard here after payment
