from project.drink.drink import Drink


class Water(Drink):
    price = 1.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.price, brand)

    def __repr__(self):
        ...

