from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        Product.__init__(self, name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters
