import pandas as pd
import random
from datetime import datetime, timedelta
import get_market_data as gmd

symbols = ['AAPL', 'NVDA', 'TSLA']

start_date = datetime(2024, 4, 1)
days = 24
records = []

curr_date = start_date
trading_days_count = 0

while trading_days_count < days:
    if curr_date.weekday() < 5:
        symbol = random.choice(symbols)
        price = gmd.get_stock_price(curr_date, symbol)
        quantity = random.randint(10, 100)
        trans_code = random.choice(['BUY', 'SELL'])

        records.append({
            'Date': curr_date.strftime('%Y-%m-%d'),
            'Ticker': symbol,
            'Price': price,
            'Quantity': quantity,
            'Trans Code': trans_code
        })
        trading_days_count += 1

    curr_date += timedelta(days=1)

df = pd.DataFrame(records)
df.to_csv('sample_trading_history.csv', index=False)

print('Successfully generated.')