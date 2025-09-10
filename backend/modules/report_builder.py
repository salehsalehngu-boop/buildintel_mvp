import os, pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

def build_excel_report(leads, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pd.DataFrame(leads).to_excel(path, index=False)

def build_pdf_report(text, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    styles = getSampleStyleSheet(); story=[Paragraph('<b>BuildIntel — Market Intelligence Report</b>', styles['Title']), Spacer(1,10)]
    for line in text.split('\n'): story += [Paragraph(line.replace('&','&amp;'), styles['BodyText']), Spacer(1,2)]
    doc.build(story)
