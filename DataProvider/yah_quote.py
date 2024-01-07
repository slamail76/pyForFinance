# Estrarre dati da yahoo data provider

import datetime as dt
import pandas_datareader as web
from pandas_datareader import data as pdr
import yfinance as yfin
from sqlalchemy import create_engine
my_conn=create_engine("mysql+pymysql://root:stefano@192.168.15.196:3306/pyfinance")

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)

ticker = ['AAPL','IP.MI','AMZN']

format = '%Y-%m-%d'
start = dt.datetime(2024, 1, 1)
start = start.strftime(format)
end = dt.datetime(2024, 1, 7)
end = end.strftime(format)

for tic in ticker:
    yfin.pdr_override()
    df = pdr.DataReader(tic, start=start, end=end)
    df.reset_index(inplace=True)
    df.insert(0, "Ticker", tic, True)
    df = trimAllColumns(df)
    df.to_sql(con=my_conn, name='shareprice', if_exists='append', index=False)
    print(df)
    #df.set_index(['Ticker', 'Date'],inplace=True)
#print(df)

#df.to_sql(con=my_conn,name='shareprice',if_exists='append',index=False)
