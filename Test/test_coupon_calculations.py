import unittest
from store import coupon_calculations as coupons

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        under_ten = 7.00
        #price: under 10, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 10), 1.80)
        #price: under 10, 5 cash, 15 %
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 15), 1.70)
        #price: under 10, 5 cash, 20%
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 20), 1.60)
        #price: under 10, 10 cash, 10%
        self.assertEqual(coupons.calculate_price(under_ten, 10.00, 10), 0)

    def test_price_under_between_ten_thirty(self):
        between_ten_thirty = 15
        #price: 10 to up to 30, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(between_ten_thirty, 5.00, 10), 9)


if __name__ == '__main__':
    unittest.main()