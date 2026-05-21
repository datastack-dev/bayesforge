import yfinance as yf
import pandas as pd
from datetime import date,timedelta
from utils.validation import clean_data

#For single assets
def load_single_asset(ticker,years):
    end_date=date.today()
    start_date=end_date-timedelta(days=years*365)
    data=yf.download(ticker,start=start_date,end=end_date)
    data=clean_data(data)
    return data
    
#For multiple assets which will tell the covariance among them
def load_multiple_assets(tickers,years):
    end_date=date.today()
    start_date=end_date-timedelta(days=365*years)
    df=pd.DataFrame()
    for ticker in tickers:
        data=yf.download(ticker,start=start_date,end=end_date)
        df[ticker]=data["Close"]
    df=clean_data(df)
    return df

#Major task in this, now how to use this data