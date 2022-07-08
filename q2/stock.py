class Stock:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name

    def get_stock_info(self) -> str:
        return self.stock_name
