import random
def collect_market_data(keywords, plan):
    data=[]; base=keywords or ['construction','tender','cement','steel']
    for k in base:
        data += [
            {'type':'tender','title':f'New {k} tender','deadline':'2025-09-15','scope':'Supply & install MEP','contact':'procurement@example.com'},
            {'type':'competitor','name':f'{k.title()} Contractors Co.','change':'Price list updated (-3% steel)','source':'competitor-site.example'},
            {'type':'material','material':'Steel rebar','price_change':'-1.2% w/w','note':'FX stabilized'}
        ]
    return data
def collect_leads(keywords, plan):
    sizes={'starter':20,'growth':80,'pro':200}; n=sizes.get(plan,20); out=[]
    for i in range(n):
        out.append({'company':f'Contractor {i+1}','industry':'Construction','role':random.choice(['Owner','Procurement Manager','Project Engineer']),
                    'email':f'contact{i+1}@contractor{i+1}.com','phone':f'+20-10{random.randint(10000000,99999999)}',
                    'linkedin':f'https://www.linkedin.com/company/contractor-{i+1}/','governorate':random.choice(['Cairo','Giza','Alexandria','Sharqia'])})
    return out
