import unittest
from store import coupon_calculations as coupons


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        under_ten = 7.00
        # price: under 10, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 10), 1.80)
        # price: under 10, 5 cash, 15 %
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 15), 1.70)
        # price: under 10, 5 cash, 20%
        self.assertEqual(coupons.calculate_price(under_ten, 5.00, 20), 1.60)
        # price: under 10, 10 cash, 10%
        self.assertEqual(coupons.calculate_price(under_ten, 10.00, 10), 0.00)

    def test_price_under_between_ten_thirty(self):
        between_ten_thirty = 15
        # price: 10 to up to 30, 15, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(between_ten_thirty, 5.00, 10), 9.00)
        # price: 10 to up to 30, 20, 5 cash, 20%
        self.assertEqual(coupons.calculate_price(between_ten_thirty + 5, 5.00, 20), 12.00)
        # price: 10 to up to 30, 28, 10 cash, 10%
        self.assertEqual(coupons.calculate_price(between_ten_thirty + 13, 10.00, 10), 16.20)

    def test_price_under_between_thirty_fifty(self):
        between_thirty_fifty = 34

        # price: 30 to up to 50, 34, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(between_thirty_fifty, 5.00, 10), 26.10)
        # price: 30 to up to 50, 32,  10 cash, 20%
        self.assertEqual(coupons.calculate_price(between_thirty_fifty - 2, 10.00, 20), 17.60)
        # price: 30 to up to 50, 45,  5 cash, 15%
        self.assertEqual(coupons.calculate_price(between_thirty_fifty + 11, 5.00, 15), 34.00)

    def test_price_under_over_fifty(self):
        over_fifty = 65

        # price: 50 and above, 5 cash, 10%
        self.assertEqual(coupons.calculate_price(over_fifty, 5.00, 10), 54)




if __name__ == '__main__':
    unittest.main()
