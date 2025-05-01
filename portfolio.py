import get_market_data as gmd

class Portfolio:
    def __init__(self, cash, positions):
        self.cash = cash
        self.positions = positions

    def buy(self, sym, amt, date):
        price = gmd.get_stock_price(date, sym)
        if amt * price <= self.cash:
            self.positions[sym] = self.positions.get(sym, 0) + amt
            self.cash -= amt * price

    def sell(self, sym, amt, date):
        price = gmd.get_stock_price(date, sym)
        if self.positions.get(sym, 0) >= amt:
            self.positions[sym] -= amt
            self.cash += amt * price

    def get_value(self, date):
        stock_value = sum([self.positions[sym] * gmd.get_stock_price(date, sym) for sym in self.positions])
        return stock_value + self.cash

    def show_portfolio(self, date):
        stock_value = sum([self.positions[sym] * gmd.get_stock_price(date, sym) for sym in self.positions])
        total_value = stock_value + self.cash
        return f'''
        Cash: ${self.cash}
        Positions: {self.positions}
        Total value: ${total_value:,.2f}
        '''