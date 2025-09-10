import pandas as pd
def clean_and_verify(leads):
    df = pd.DataFrame(leads)
    if df.empty: return []
    df = df.drop_duplicates(subset=['email'])
    df = df[df['email'].str.contains('@')]
    return df.to_dict(orient='records')
