def calculate_price(price, cash_coupon, percent_coupon):


    #self.assertEqual(coupons.calculate_price(under_ten, 5.00, 10) == 1.80)
    cc_discount_price = price - cash_coupon
    percent_value = percent_coupon / 100

    #subtract percent value from the CC_discount_price
    discount_price = cc_discount_price * (1 - percent_value)

    if cc_discount_price <= 0:
        return 0.00
    #((price - cash_coupon) * (1 - percent_coupon / 100))

    return discount_price




if __name__ == '__main__':
    pass
    #calculate_price()

