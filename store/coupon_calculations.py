def calculate_price(price, cash_coupon, percent_coupon):

    #self.assertEqual(coupons.calculate_price(under_ten, 5.00, 10) == 1.80)
    cc_discount_price = price - cash_coupon
    percent_value = percent_coupon / 100

    #subtract percent value from the CC_discount_price
    discount_value = cc_discount_price * (1 - percent_value)


    return




if __name__ == '__main__':
    pass
    #calculate_price()

