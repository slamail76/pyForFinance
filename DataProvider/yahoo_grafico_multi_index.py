import datetime as dt
import pandas_datareader as web
from pandas_datareader import data as pdr
import yfinance as yfin
import matplotlib.pyplot as plt

format = '%Y-%m-%d'
start = dt.datetime(2015, 1, 1)
start = start.strftime(format)
end = dt.datetime(2023, 12, 28)
end = end.strftime(format)
print(start)
print(end)
index = ["^DJI", "IP.MI"]
plt.figure(figsize=(8,4), dpi=100)
plt.title('Multi index graph')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("High")

count = 0
for ind in index:
    count += 1
    yfin.pdr_override()
    df = pdr.DataReader(ind, start=start, end=end)
    df.reset_index(inplace=True)
    x = df['Date']
    y = df['High']
    print(x,y)
    if count == 1:
        plt.plot(x,y,'red')
    elif count == 2:
        plt.plot(x, y, 'blue')

plt.show()