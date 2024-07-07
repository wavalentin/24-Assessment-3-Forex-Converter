import unittest
from app import app


class CurrencyConversionTestCase(unittest.TestCase):
    def setUp(self):
        app.test = True
        self.app = app.test_client()

    def test_conversion(self):
        response = self.app.post('/convert', data=dict(
            from_currency='USD',
            to_currency='USD',
            amount=1
        ))
        data = response.data.decode('utf-8')
        self.assertIn('1 USD', data)
        self.assertIn('1 USD', data)
        self.assertIn('results', data)


if __name__ == '__main__':
    unittest.main()
