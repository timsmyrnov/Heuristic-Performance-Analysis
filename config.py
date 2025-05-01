import pandas as pd
from portfolio import Portfolio
import get_market_data as gmd

class Config:
    def __init__(self, file_name: str):
        try:
            df = pd.read_csv(f'{file_name}')
        except FileNotFoundError:
            print(f'No file named "{file_name}" was found in the root folder.')
            return

        df.columns = df.columns.str.lower()

        req_columns = ['date', 'ticker', 'quantity', 'price', 'trans code']
        if not all(col in df.columns for col in req_columns):
            print(f"The file must contain the following columns: {', '.join(req_columns)}")
            return

        df['date'] = pd.to_datetime(df['date'])
        df['quantity'] = df['quantity'].astype(int)

        start_date = df['date'].min()
        end_date = df['date'].max()

        self.start_date = start_date.strftime('%Y-%m-%d')
        self.end_date = end_date.strftime('%Y-%m-%d')
        self.symbols = list(sorted(df['ticker'].unique()))
        print('What\'s the starting portfolio value? (e.g. 1000)')
        self.start_value = float(input('$'))

        # Compute end value
        prt = Portfolio(self.start_value, {})

        for _, row in df.iterrows():
            date = row['date'].strftime('%Y-%m-%d')
            ticker = row['ticker']
            qty = row['quantity']
            trans_code = row['trans code'].lower()

            if trans_code == 'buy':
                prt.buy(ticker, qty, date)
            elif trans_code == 'sell':
                prt.sell(ticker, qty, date)

        self.end_value = prt.get_value(self.end_date)

    def show_cfg(self):
        return f'''
        Trading start date: {self.start_date}
        Trading end date: {self.end_date}
        Starting portfolio value: ${self.start_value:,.2f}
        Final portfolio value: ${self.end_value:,.2f}
        Profit: ${self.end_value - self.start_value:,.2f}
        '''