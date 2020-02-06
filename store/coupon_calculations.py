def calculate_price(price, cash_coupon, percent_coupon):
    pass

price = int( input('Please enter price: '))
cash_coupon = int( input('Please enter cash coupon amount: '))

if cash_coupon > 0:
    total_price_cash_coupon = price - cash_coupon
    print('Your total is $%0d' % (total_price_cash_coupon))
if __name__ == '__main__':
    calculate_price()