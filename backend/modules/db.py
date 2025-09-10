import json, os, datetime
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
CONFIG = os.path.join(BASE,'config'); OUTPUT=os.path.join(BASE,'output'); os.makedirs(OUTPUT, exist_ok=True)
CLIENTS_FILE=os.path.join(CONFIG,'clients.json'); RUNS_FILE=os.path.join(CONFIG,'runs.json')
def load_clients(): return json.load(open(CLIENTS_FILE,'r',encoding='utf-8')) if os.path.exists(CLIENTS_FILE) else []
def save_clients(c): json.dump(c, open(CLIENTS_FILE,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
def mark_client_paid(email): c=load_clients(); [x.update({'paid':True}) for x in c if x.get('email')==email]; save_clients(c)
def record_run(email, excel, pdf, items): 
    runs = json.load(open(RUNS_FILE,'r',encoding='utf-8')) if os.path.exists(RUNS_FILE) else []
    runs.append({'email':email,'excel':excel,'pdf':pdf,'items':items,'ts':datetime.datetime.now().isoformat()})
    json.dump(runs, open(RUNS_FILE,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
