"""
2.類別與模組化
- stock.py:
- 1. 建構一個Stock的類別，並設定在初始化時需傳入參數stock_name(string)。
- 2. 定義方法get_stock_info()，回傳已經定義好的stock_name。
Ans.
- main.py
- 1. 創造Stock類別的物件，同時傳入stock_name為'tesla'
- 2. 呼叫Stock類別的方法get_stock_info()。
"""
from stock import Stock

if __name__ == '__main__':
    stock = Stock('tesla')
    print(stock.get_stock_info())
