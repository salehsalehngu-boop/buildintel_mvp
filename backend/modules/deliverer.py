import os, smtplib, mimetypes
from email.message import EmailMessage
def deliver_email(to_email, subject, body, attachments=None):
    server=os.getenv('SMTP_SERVER'); port=int(os.getenv('SMTP_PORT','587')); user=os.getenv('SMTP_USER'); pwd=os.getenv('SMTP_PASSWORD'); from_email=os.getenv('FROM_EMAIL', user)
    if not all([server,port,user,pwd,from_email]): print('SMTP not configured; skipping email.'); return
    msg=EmailMessage(); msg['From']=from_email; msg['To']=to_email; msg['Subject']=subject; msg.set_content(body)
    for p in attachments or []:
        ctype,_=mimetypes.guess_type(p); ctype=ctype or 'application/octet-stream'; maintype,subtype=ctype.split('/',1); msg.add_attachment(open(p,'rb').read(), maintype=maintype, subtype=subtype, filename=os.path.basename(p))
    with smtplib.SMTP(server, port) as s: s.starttls(); s.login(user,pwd); s.send_message(msg); print(f'Email sent to {to_email}.')
def deliver_whatsapp(num, message, media=None): print(f'(WHATSAPP) {num}: {message} | media={media}')
def deliver_reports(client, excel_path, pdf_path):
    deliver_email(client['email'], 'Your BuildIntel Report', 'Attached: latest report & leads.', [pdf_path, excel_path])
    if client.get('whatsapp'): deliver_whatsapp(client['whatsapp'], 'BuildIntel: Your latest reports are ready.', [pdf_path, excel_path])
