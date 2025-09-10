from .modules.db import load_clients, record_run
from .modules.scrapers import collect_market_data, collect_leads
from .modules.cleaner import clean_and_verify
from .modules.summarizer import summarize_insights
from .modules.report_builder import build_excel_report, build_pdf_report
from .modules.deliverer import deliver_reports
from datetime import datetime

def run_pipeline_for_client(client: dict):
    plan = client.get('plan','starter'); kws = client.get('keywords',[])
    market = collect_market_data(keywords=kws, plan=plan)
    leads = clean_and_verify(collect_leads(keywords=kws, plan=plan))
    summary = summarize_insights(market, plan)
    ts = datetime.now().strftime('%Y%m%d_%H%M')
    excel = f'output/{client.get("company","Client")}_leads_{ts}.xlsx'
    pdf = f'output/{client.get("company","Client")}_intel_{ts}.pdf'
    build_excel_report(leads, excel); build_pdf_report(summary, pdf)
    deliver_reports(client, excel, pdf); record_run(client['email'], excel, pdf, len(leads))

def run_pipeline_for_all_clients():
    for c in load_clients():
        if c.get('active', True) and c.get('paid', True): run_pipeline_for_client(c)
