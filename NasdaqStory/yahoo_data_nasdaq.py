# Estrarre dati da yahoo data provider

import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

start = dt.datetime(1980, 10, 1)
end = dt.datetime(2021, 11, 23)
df = web.DataReader('^IXIC', 'yahoo', start, end)
print(df)

df.reset_index(inplace=True)
x = df['Date']
y = df['High']
print(x,y)


plt.figure(figsize=(8,4), dpi=100)

plt.plot(x,y,'red')
plt.xlabel("Tempo")
plt.ylabel("High")
plt.title('Curva del Nasdaq')
plt.grid()
plt.show()
