from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    from_table = 0
    to_table = 1

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not self.from_table <= value <= self.to_table:
            raise ValueError(f"Outside table's number must be between {self.from_table} and {self.to_table} inclusive!")
        self.__table_number = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...

    @abstractmethod
    def order_food(self, baked_food: BakedFood):
        ...

    @abstractmethod
    def order_drink(self, drink: Drink):
        ...

    @abstractmethod
    def get_bill(self):
        ...

    @abstractmethod
    def clear(self):
        ...

    @abstractmethod
    def free_table_info(self):
        ...

