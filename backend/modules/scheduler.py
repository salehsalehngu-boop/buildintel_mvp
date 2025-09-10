from apscheduler.triggers.cron import CronTrigger
from .db import load_clients
from ..main import run_pipeline_for_client
def _add_job_for_client(s, c):
    plan=c.get('plan','starter')
    if plan=='starter': trig=CronTrigger(day=1,hour=8,minute=0,timezone='Africa/Cairo')
    elif plan=='growth': trig=CronTrigger(day_of_week='mon',hour=8,minute=0,timezone='Africa/Cairo')
    else: trig=CronTrigger(hour=7,minute=30,timezone='Africa/Cairo')
    s.add_job(run_pipeline_for_client, trig, args=[c], id=f"client_{c['email']}", replace_existing=True)
def register_jobs(s):
    for c in load_clients():
        if c.get('active', True) and c.get('paid', True): _add_job_for_client(s, c)
