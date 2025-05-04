import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from monkey_trade import MonkeyTrade

class TestMonkeyTrade(unittest.TestCase):

    @patch('monkey_trade.Portfolio')
    @patch('monkey_trade.gmd.get_stock_price')
    def test_monkey_buy_success(self, mock_get_price, mock_portfolio):
        mock_get_price.return_value = 100
        portfolio_instance = mock_portfolio.return_value
        portfolio_instance.cash = 1000

        trader = MonkeyTrade('2023-01-01', '2023-01-10', 1000, ['AAPL', 'GOOG'])
        trader.prt = portfolio_instance

        date = datetime.strptime('2023-01-03', '%Y-%m-%d')
        trader.monkey_buy(date)

        self.assertTrue(portfolio_instance.buy.called)

    @patch('monkey_trade.Portfolio')
    @patch('monkey_trade.gmd.get_stock_price')
    def test_monkey_buy_insufficient_funds(self, mock_get_price, mock_portfolio):
        mock_get_price.return_value = 2000
        portfolio_instance = mock_portfolio.return_value
        portfolio_instance.cash = 1000

        trader = MonkeyTrade('2023-01-01', '2023-01-10', 1000, ['AAPL'])
        trader.prt = portfolio_instance

        date = datetime.strptime('2023-01-03', '%Y-%m-%d')
        trader.monkey_buy(date)

        self.assertFalse(portfolio_instance.buy.called)

    @patch('monkey_trade.Portfolio')
    def test_monkey_sell_with_position(self, mock_portfolio):
        portfolio_instance = mock_portfolio.return_value
        portfolio_instance.positions = {'AAPL': 10}

        trader = MonkeyTrade('2023-01-01', '2023-01-10', 1000, ['AAPL'])
        trader.prt = portfolio_instance

        date = datetime.strptime('2023-01-03', '%Y-%m-%d')
        trader.monkey_sell(date)

        self.assertTrue(portfolio_instance.sell.called)

    @patch('monkey_trade.Portfolio')
    def test_monkey_sell_nothing_to_sell(self, mock_portfolio):
        portfolio_instance = mock_portfolio.return_value
        portfolio_instance.positions = {}

        trader = MonkeyTrade('2023-01-01', '2023-01-10', 1000, ['AAPL'])
        trader.prt = portfolio_instance

        date = datetime.strptime('2023-01-03', '%Y-%m-%d')
        trader.monkey_sell(date)

        self.assertFalse(portfolio_instance.sell.called)

    @patch('monkey_trade.Portfolio')
    def test_show_results(self, mock_portfolio):
        portfolio_instance = mock_portfolio.return_value
        portfolio_instance.get_value.return_value = 1200

        trader = MonkeyTrade('2023-01-01', '2023-01-10', 1000, ['AAPL'])
        trader.prt = portfolio_instance

        result = trader.show_results()
        self.assertIn('Starting monkey portfolio value', result)
        self.assertIn('Profit: $200.00', result)

if __name__ == '__main__':
    unittest.main()