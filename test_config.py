import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from config import Config

class TestConfig(unittest.TestCase):

    @patch('builtins.input', return_value='1000')
    @patch('config.gmd.get_stock_price')
    @patch('config.pd.read_csv')
    def test_valid_config(self, mock_read_csv, mock_get_price, mock_input):
        mock_df = pd.DataFrame({
            'Date': ['2024-01-01', '2024-01-02'],
            'Ticker': ['AAPL', 'AAPL'],
            'Quantity': [5, 2],
            'Price': [100, 110],
            'Trans Code': ['buy', 'sell']
        })

        mock_read_csv.return_value = mock_df
        mock_get_price.side_effect = lambda date, sym: 100

        cfg = Config('dummy.csv')

        self.assertEqual(cfg.start_date, '2024-01-01')
        self.assertEqual(cfg.end_date, '2024-01-02')
        self.assertEqual(cfg.symbols, ['AAPL'])
        self.assertEqual(cfg.start_value, 1000.0)
        self.assertIsInstance(cfg.end_value, float)
        self.assertGreaterEqual(cfg.end_value, 0)

        summary = cfg.show_cfg()
        self.assertIn('Trading start date: 2024-01-01', summary)
        self.assertIn('Final portfolio value:', summary)

    @patch('config.pd.read_csv', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_read_csv):
        with patch('builtins.print') as mock_print:
            cfg = Config('nonexistent.csv')
            mock_print.assert_called_with('No file named "nonexistent.csv" was found in the root folder.')

    @patch('builtins.input', return_value='1000')
    @patch('config.pd.read_csv')
    def test_missing_columns(self, mock_read_csv, mock_input):
        mock_df = pd.DataFrame({
            'Wrong': [1], 'Cols': [2]
        })
        mock_read_csv.return_value = mock_df

        with patch('builtins.print') as mock_print:
            cfg = Config('bad.csv')
            mock_print.assert_called_with("The file must contain the following columns: date, ticker, quantity, price, trans code")

if __name__ == '__main__':
    unittest.main()