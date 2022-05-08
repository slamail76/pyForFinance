# Yahoo Ticker Scraper V.1.0.0 - Year 2021.11 - Programmer Stefano Lama

import pandas as pd
import requests
from settori import sector_find
from sqlalchemy import create_engine
from yah_urlmaker import urladdress

off = 0      # valore di partenza
count = 250  # valore di step massimo
my_conn = create_engine("mysql+mysqldb://root:stefano@192.168.15.194:3306/pyfinance")
headers = {'User-agent': 'Mozilla/5.0'}
dfs = pd.DataFrame()


def ticker_insert(url_i, limite_i, off_i, count_i):
    while off_i < limite_i:
        print("Running   ..........")
        site = str(url_i)+"?offset="+str(off_i)+"&count="+str(count_i)
        print(site)
        """
        site = "https://finance.yahoo.com/screener/predefined/top_mutual_funds" \
           "?offset=" + str(offset) + "&count=" + str(count) + ""
        """
        dfo = pd.read_html(requests.get(site, headers=headers).text)[0]
        dfs[['Ticker', 'Company']] = dfo[['Symbol', 'Name']]
        dfs.dropna(subset=['Ticker', 'Company'], inplace=True)

        #dfs.style.set_properties(**{'text-align': 'left'})

        #dfs.to_sql(con=my_conn, name='tickers', if_exists=
        # append', index=False)
        # print(dfo)
        off_i += 250


# INIZIO PROGRAMMA V1.0.0 SL
print("PROGRAMMA PER INSERIRE I TICKERS DI YAHOO FINANCE SU MARIADB")
print("")
regione = str(input("Inserisci la regione es. (IT) "))
print("1) Basic Material\n2) Financial Services\n3) Consumer Defensive\n4) Utilities\n5) Energy\n"
      "6) Technology\n7) Consumer Cyclical\n8) Real Estate\n9) HelthCare\n10)Communication Services\n11)Industrials")
sector = int(input("Inserisci il numero del settore interessato = "))
settore = sector_find(sector)
url = urladdress(regione, settore)
url1 = url[0]
limite = url[1]
ticker_insert(url1, limite, off, count)
print("Terminato")
