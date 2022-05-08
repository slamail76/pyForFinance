# Estrarre dati da yahoo data provider

import datetime as dt
import pandas_datareader as web
from sqlalchemy import create_engine
my_conn=create_engine("mysql+pymysql://root:stefano@192.168.15.194:3306/pyfinance")

def trimAllColumns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trimStrings = lambda x: x.strip() if type(x) is str else x
    return df.applymap(trimStrings)

ticker = ['AAPL','FB','AMZN']
# Inizializzazione variabile data di inizio
start = dt.datetime(2021, 10, 1)
# Inizializzazione variabile data di fine
end = dt.datetime(2021, 11, 4)

for tic in ticker:
    df = web.DataReader(tic, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.insert(0, "Ticker", tic, True)
    df = trimAllColumns(df)
    df.to_sql(con=my_conn, name='shareprice', if_exists='append', index=False)
    print(df)
    #df.set_index(['Ticker', 'Date'],inplace=True)
#print(df)

#df.to_sql(con=my_conn,name='shareprice',if_exists='append',index=False)
