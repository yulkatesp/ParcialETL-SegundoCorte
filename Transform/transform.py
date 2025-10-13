import pandas as pd

class Transformer:

    def __init__(self, df):
        self.df = df

    def clean(self):

        df = self.df.copy()
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date', 'Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8'])

        text_cols = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown')

        self.df = df
        return self.df