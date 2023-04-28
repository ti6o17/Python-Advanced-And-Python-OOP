from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.table.table import Table


class OutsideTable(Table):
    from_table = 51
    to_table = 100

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    def reserve(self, number_of_people: int):
        if number_of_people <= self.capacity:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        sum_drinks = sum([drink.price for drink in self.drink_orders])
        sum_food = sum([food.price for food in self.food_orders])
        price = sum_drinks + sum_food
        return price

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"\nTable: {self.table_number}\nType: " \
                     f"{self.__class__.__name__}\nCapacity: {self.capacity}"
            return result
