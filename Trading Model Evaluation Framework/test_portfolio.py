import unittest
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    def test_initial_display(self):
        p = Portfolio(1000, {"AAPL": 5})
        self.assertEqual(p.display(), (1000, {"AAPL": 5}))

    def test_buy_with_enough_cash(self):
        p = Portfolio(1000, {})
        p.buy("AAPL", 5, 100)
        self.assertEqual(p.cash, 500)
        self.assertEqual(p.positions, {"AAPL": 5})

    def test_buy_with_insufficient_cash(self):
        p = Portfolio(200, {})
        p.buy("AAPL", 5, 100)
        self.assertEqual(p.cash, 200)
        self.assertEqual(p.positions, {})

    def test_sell_with_enough_shares(self):
        p = Portfolio(500, {"TSLA": 10})
        p.sell("TSLA", 5, 50)
        self.assertEqual(p.cash, 750)
        self.assertEqual(p.positions, {"TSLA": 5})

    def test_sell_with_insufficient_shares(self):
        p = Portfolio(500, {"TSLA": 2})
        p.sell("TSLA", 5, 50)
        self.assertEqual(p.cash, 500)
        self.assertEqual(p.positions, {"TSLA": 2})

    def test_sell_unowned_stock(self):
        p = Portfolio(500, {})
        with self.assertRaises(KeyError):
            p.sell("GOOG", 1, 100)

    def test_buy_then_sell_combo(self):
        p = Portfolio(1000, {})
        p.buy("NFLX", 4, 200)
        p.sell("NFLX", 2, 250)
        self.assertEqual(p.cash, 700)
        self.assertEqual(p.positions, {"NFLX": 2})

    def test_multiple_buys(self):
        p = Portfolio(1000, {})
        p.buy("AAPL", 2, 100)
        p.buy("AAPL", 3, 100)
        self.assertEqual(p.positions, {"AAPL": 5})
        self.assertEqual(p.cash, 500)

if __name__ == '__main__':
    unittest.main()