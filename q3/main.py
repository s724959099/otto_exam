"""
1) 新增一個欄位(DailyReturn)，計算每日收盤價(Close)的變動率(今日收盤價-昨日收盤價/昨
日收盤價的百分比)
Ans.
2) 收盤價(Close)的均值與標準差為何?
Ans.
3) 找出收盤價(Close)範圍為均值與一個標準差以內的資料，並儲存於新的資料表中(df_new)
"""
import pandas as pd

df = pd.read_csv('./BTCUSDT-4h-data.csv')
# ans1
df['DailyReturn'] = df['close'].pct_change()
# ans2 - 1
avg = df['close'].mean()
print(avg)
# ans2 - 2
std = df['close'].std()
print(std)
# ans 3
df_new = df[(df['close'] > avg - std) & (df['close'] < avg + std)]
df_new.to_csv('./BTCUSDT-4h-data-new.csv')
