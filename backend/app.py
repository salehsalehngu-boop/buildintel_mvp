from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os, hmac, hashlib
from .main import run_pipeline_for_all_clients
from .modules.scheduler import register_jobs
from .modules.db import mark_client_paid

load_dotenv()
app = FastAPI(title="BuildIntel Backend", version="1.0.0")
scheduler = BackgroundScheduler(timezone="Africa/Cairo"); scheduler.start(); register_jobs(scheduler)

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/run')
def manual_run():
    run_pipeline_for_all_clients()
    return {'status':'queued'}

def verify(body: bytes, secret: str, sig: str) -> bool:
    import hmac, hashlib
    mac = hmac.new(secret.encode(), body, hashlib.sha512).hexdigest()
    return hmac.compare_digest(mac, sig or '')

@app.post('/webhook/paymob')
async def webhook(request: Request):
    body = await request.body()
    secret = os.getenv('PAYMOB_HMAC_SECRET') or ''
    sig = request.headers.get('Hmac-Signature','')
    if not secret or not verify(body, secret, sig):
        raise HTTPException(401, 'Invalid HMAC')
    payload = await request.json()
    email = payload.get('customer',{}).get('email')
    if not email: raise HTTPException(400,'Missing email')
    mark_client_paid(email); return JSONResponse({'ok':True})
