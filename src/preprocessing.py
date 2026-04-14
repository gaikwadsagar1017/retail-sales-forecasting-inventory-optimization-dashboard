import pandas as pd

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df.ffill()   # ✅ fixed
    return df