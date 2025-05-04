import unittest
from unittest.mock import patch
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    @patch('portfolio.gmd.get_stock_price')
    def test_buy_zero_amount(self, mock_get_price):
        mock_get_price.return_value = 100
        p = Portfolio(1000, {})
        p.buy('AAPL', 0, '2024-01-01')
        self.assertEqual(p.cash, 1000)
        self.assertNotIn('AAPL', p.positions)

    @patch('portfolio.gmd.get_stock_price')
    def test_buy_negative_amount(self, mock_get_price):
        mock_get_price.return_value = 100
        p = Portfolio(1000, {})
        p.buy('AAPL', -5, '2024-01-01')
        self.assertEqual(p.cash, 1000)
        self.assertNotIn('AAPL', p.positions)

    @patch('portfolio.gmd.get_stock_price')
    def test_sell_zero_amount(self, mock_get_price):
        mock_get_price.return_value = 50
        p = Portfolio(500, {'AAPL': 5})
        p.sell('AAPL', 0, '2024-01-01')
        self.assertEqual(p.cash, 500)
        self.assertEqual(p.positions['AAPL'], 5)

    @patch('portfolio.gmd.get_stock_price')
    def test_sell_negative_amount(self, mock_get_price):
        mock_get_price.return_value = 50
        p = Portfolio(500, {'AAPL': 5})
        p.sell('AAPL', -3, '2024-01-01')
        self.assertEqual(p.cash, 500)
        self.assertEqual(p.positions['AAPL'], 5)

    @patch('portfolio.gmd.get_stock_price')
    def test_get_value_no_positions(self, mock_get_price):
        p = Portfolio(250, {})
        total = p.get_value('2024-01-01')
        self.assertEqual(total, 250)

    @patch('portfolio.gmd.get_stock_price')
    def test_show_portfolio_no_positions(self, mock_get_price):
        p = Portfolio(400, {})
        summary = p.show_portfolio('2024-01-01')
        self.assertIn('Cash: $400', summary)
        self.assertIn("Positions: {}", summary)
        self.assertIn('Total value: $400.00', summary)

    @patch('portfolio.gmd.get_stock_price')
    def test_partial_buy(self, mock_get_price):
        mock_get_price.return_value = 50
        p = Portfolio(100, {})
        p.buy('AAPL', 2, '2024-01-01')
        self.assertEqual(p.cash, 0)
        self.assertEqual(p.positions['AAPL'], 2)

    @patch('portfolio.gmd.get_stock_price')
    def test_price_fluctuation_effect_on_value(self, mock_get_price):
        p = Portfolio(0, {'AAPL': 2})
        mock_get_price.return_value = 100
        val1 = p.get_value('2024-01-01')
        self.assertEqual(val1, 200)

        mock_get_price.return_value = 150
        val2 = p.get_value('2024-01-02')
        self.assertEqual(val2, 300)

if __name__ == '__main__':
    unittest.main()
