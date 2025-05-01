import config as cfg
import yfinance as yf
import pandas as pd
from datetime import datetime

symbols = [
    "NVDA", "HTZ", "F", "INTC", "PLTR", "TSLA", "ABEV", "LCID", "BTG", "PFE",
    "AAL", "AAPL", "SXTC", "BAC", "SOFI", "RIG", "AMZN", "JBLU", "AGNC", "SMX",
    "MSGM", "APLD", "AMD", "NU", "GOOGL", "PBR", "NVO", "SNAP", "WBD", "HBAN",
    "AMCR", "VRN", "BBAI", "UNH", "TSM", "SMCI", "VALE", "ERIC", "BBD", "T",
    "LYG", "HOOD", "NGD", "NIO", "KMI", "KVUE", "AVGO", "HPE", "AGL", "UBER",
    "CMCSA", "CSX", "MRK", "WMT", "CLSK", "ITUB", "MSFT", "UUUU", "ACHR", "RIOT",
    "WOLF", "KO", "INFY", "MU", "QXO", "MP", "CNH", "GOLD", "KGC", "GOOG", "MARA",
    "FNA", "SCHW", "KEY", "WFC", "NKE", "TGL", "RF", "PTEN", "HIMS", "STLA",
    "SBSW", "HAL", "IAG", "XOM", "BABA", "AG", "GRAB"
]

start_date = '2000-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

data = yf.download(symbols, start=start_date, end=end_date, group_by='symbol')
combined_data = pd.DataFrame()

for sym in symbols:
    temp_df = data[sym].reset_index()
    temp_df['Symbol'] = sym
    temp_df = temp_df[['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume']]
    combined_data = pd.concat([combined_data, temp_df], ignore_index=True)

numerical_columns = ['Open', 'High', 'Low', 'Close']
combined_data[numerical_columns] = combined_data[numerical_columns].round(2)

combined_data.to_csv('market_data.csv', index=False)