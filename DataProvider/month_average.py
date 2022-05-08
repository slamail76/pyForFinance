import datetime as dt
from datetime import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
listaanni =[]


def explodeyears(styear, endyear):
    anni = startyear
    listaanni.append(anni)
    while anni < endyear:
        anni += 1
        listaanni.append(anni)
    return(listaanni)

""" Esempio per estrarre anno mese giorno
date = '2021-05-21 11:22:03'
datem = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
print(datem.day)        # 25
print(datem.month)      # 5
print(datem.year)       # 2021
print(datem.hour)       # 11
print(datem.minute)     # 22
"""

startyear = 1980
startmonth = 1
startday = 1

endyear = 2021
endmonth = 12
endday = 31
years = endyear-startyear
i = 0

start = dt.datetime(startyear, startmonth, startday)
end = dt.datetime(endyear, endmonth, endday)
df = web.DataReader('^DJI', 'yahoo', start, end)
df.reset_index(inplace=True)
#print(df)
#dfrows = len(df.index)

for ann in explodeyears(startyear, endyear):
   for index, row in df.iterrows():
       date = str((row['Date']))
       datem = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
       yeardf = datem.year
       if yeardf == ann:
           for m in range(1,12):
               if datem.month == m:
                   print(df)

               else:
                   break
#print(explodeyears(startyear, endyear))

x = df['Date']
y = df['Adj Close']