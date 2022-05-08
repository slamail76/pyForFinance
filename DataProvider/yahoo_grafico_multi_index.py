import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2021, 11, 28)
index = ['^DJI', '^IXIC']
plt.figure(figsize=(8,4), dpi=100)
plt.title('Multi index graph')
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("High")

count = 0
for ind in index:
    count += 1
    df = web.DataReader(ind, 'yahoo', start, end)
    df.reset_index(inplace=True)
    x = df['Date']
    y = df['High']
    print(x,y)
    if count == 1:
        plt.plot(x,y,'red')
    elif count == 2:
        plt.plot(x, y, 'blue')


plt.show()