class Cart:

    def __init__(self, goods_prices):
        self.goods_prices = goods_prices
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return sum(self.goods_prices)


if __name__ == '__main__':
    cart_1 = Cart([1000, 2000, 3000])
    print(cart_1.total_price)
