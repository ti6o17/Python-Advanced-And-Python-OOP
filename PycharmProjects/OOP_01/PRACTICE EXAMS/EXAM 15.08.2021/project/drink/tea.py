from project.drink.drink import Drink


class Tea(Drink):
    price = 2.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.price, brand)

    def __repr__(self):
        ...

