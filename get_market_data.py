import pandas as pd

def get_stock_price(date: str, stock: str):
    try:
        date_dt = pd.to_datetime(date)
        df = pd.read_csv('market_data.csv', parse_dates=['Date'])
        result = df[(df['Date'] == date_dt) & (df['Symbol'] == stock.upper())]

        if not result.empty:
            return float(result.iloc[0]['Close'])
        else:
            print('No data found for the given date and stock.')
            return None
    except FileNotFoundError:
        print('The file "market_data.csv" was not found.')
        return None
    
if __name__ == '__main__':
    print(get_stock_price('2024-04-02', 'NVDA'))