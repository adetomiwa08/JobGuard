# x402.py
from fastapi.responses import JSONResponse

def x402_response():
    return JSONResponse(
        status_code=402,
        content={
            "x402Version": 1,
            "accepts": [
                {
                    "scheme": "exact",
                    "network": "base",
                    "maxAmountRequired": "0",
                    "resource": "/scan",
                    "description": "Analyze job postings for scam risk and safety",
                    "mimeType": "application/json",
                    "payTo": "0x0000000000000000000000000000000000000000",
                    "maxTimeoutSeconds": 300,
                    "asset": "ETH"
                }
            ]
        }
    )
