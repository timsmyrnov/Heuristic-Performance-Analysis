from portfolio import Portfolio
import get_market_data as gmd
from datetime import datetime, timedelta
import random

class MonkeyTrade:
    def __init__(self, start_date, end_date, cash, symbols):
        self.start_value = cash
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.days = (self.end_date - self.start_date).days + 1
        self.syms = symbols
        self.prt = Portfolio(cash, {})

    def monkey_buy(self, date):
        print(f'\nDay {(date - self.start_date).days + 1}, {date.strftime("%Y-%m-%d")}. *Buy*')

        sym = random.choice(self.syms)
        max_amt = int(self.prt.cash // gmd.get_stock_price(date, sym))

        if max_amt > 0:
            amt = random.randint(1, max_amt)
            self.prt.buy(sym, amt, date)
            print(f'[{amt} {sym}]')
        else:
            print(f'(insufficient funds)')


    def monkey_sell(self, date):
        print(f'\nDay {(date - self.start_date).days + 1}, {date.strftime("%Y-%m-%d")}. *Sell*')

        if self.prt.positions != {}:
            sym = random.choice(list(self.prt.positions.keys()))
            max_amt = self.prt.positions.get(sym, 0)
            
            if max_amt > 0:
                amt = random.randint(1, max_amt)
                self.prt.sell(sym, amt, date)
                print(f'[{amt} {sym}]')

                if amt == max_amt:
                    del self.prt.positions[sym]
            else:
                print(f'(nothing to sell)')
        else:
            print(f'(nothing to sell)')

    def monkey_hold(self, date):
        print(f'\nDay {(date - self.start_date).days + 1}, {date.strftime("%Y-%m-%d")}. *Hold*')

    def monkey_trade(self):
        for d in range(1, self.days + 1):
            date = self.start_date + timedelta(days=d)

            if date.weekday() < 5:
                random.choice([self.monkey_buy, self.monkey_sell, self.monkey_hold])(date)
            else:
                print(f'\nDay {(date - self.start_date).days + 1}, {date.strftime("%Y-%m-%d")}. *Hold* (weekend)')

    def show_results(self):
        final_value = self.prt.get_value(self.end_date)
        profit = final_value - self.start_value

        return f'''
        Starting monkey portfolio value: ${self.start_value:,.2f}
        Final monkey portfolio value: {final_value:,.2f}
        Profit: ${profit:,.2f}
        '''
    
if __name__ == '__main__':
    m = MonkeyTrade('2024-04-01', '2024-04-30', 100_000, ['AAPL', 'NVDA', 'MSFT', 'GOOG', 'TSLA'])
    m.monkey_trade()
    print(m.show_results())