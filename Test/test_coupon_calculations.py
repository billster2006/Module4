import unittest
#import unittest.mock as mock
from store import coupon_calculations as coupons

class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        dollar_amt = 7.00
        assert coupons.calculate_price(dollar_amt, 5, 10) == 1.80
        assert coupons.calculate_price(dollar_amt, 5, 15) == 1.70
        assert coupons.calculate_price(dollar_amt, 5, 20) == 1.60
        assert coupons.calculate_price(dollar_amt, 10, 10) == 0



if __name__ == '__main__':
    unittest.main()