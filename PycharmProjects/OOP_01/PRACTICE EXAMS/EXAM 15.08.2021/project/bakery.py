from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    POSSIBLE_TYPES_OF_FOOD = {
        "Bread": Bread,
        "Cake": Cake
    }

    POSSIBLE_TYPES_OF_DRINKS = {
        "Water": Water,
        "Tea": Tea
    }

    POSSIBLE_TYPES_OF_TABLES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.table_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if not self.food_menu:
            self.food_menu.append(self.POSSIBLE_TYPES_OF_FOOD[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"
        for food in self.food_menu:
            if food.name == name:
                return Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(self.POSSIBLE_TYPES_OF_FOOD[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if not self.drinks_menu:
            self.drinks_menu.append(self.POSSIBLE_TYPES_OF_DRINKS[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"
        for drink in self.drinks_menu:
            if drink.name == name:
                return Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(self.POSSIBLE_TYPES_OF_DRINKS[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if not self.table_repository:
            self.table_repository.append(self.POSSIBLE_TYPES_OF_TABLES[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

        for table in self.table_repository:


            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
            self.food_menu.append(self.POSSIBLE_TYPES_OF_TABLES[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.table_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
            return f"No available table for {number_of_people} people"

    def _find_table(self, table_number):
        for table in self.table_repository:
            if table.is_reserved and table.table_number == table_number:
                return table

    @staticmethod
    def _find_if_item_in_menu(item_name, items_menu):
        for item in items_menu:
            x = item.name
            y = item_name
            if item.name == item_name:
                return item
            return None

    def order_food(self, table_number: int, *food_name):
        if not self._find_table(table_number):
            raise Exception(f"Could not find table {table_number}")
        table = self._find_table(table_number)
        food_not_in_menu = []
        for name in food_name:
            food = self._find_if_item_in_menu(name, self.food_menu)
            if food:
                table.food_orders.append(food)
            else:
                food_not_in_menu.append(name)
        result = f"Table {table_number} ordered:\n"
        for i in range(len(table.food_orders)):
            if i == len(table.food_orders) - 1:
                result += f"- {[food.name for food in table.food_orders][i]}: " \
                          f"{[food.portion for food in table.food_orders][i]}g" \
                          f" - {[food.price for food in table.food_orders][i]}lv\n"
            else:
                result += f"- {[food.name for food in table.food_orders][i]}: " \
                          f"{[food.portion for food in table.food_orders][i]}g" \
                          f" - {[food.price for food in table.food_orders][i]}lv"
        result += f'{self.name} does not have in the menu:\n'
        for i in range(len(food_not_in_menu)):
            if not i == len(food_not_in_menu) - 1:
                result += f'{[food for food in food_not_in_menu][i]}\n'
            else:
                result += f'{[food for food in food_not_in_menu][i]}'
        return result

    def order_drinks(self, table_number: int, *drinks_name):
        if not self._find_table(table_number):
            raise Exception(f"Could not find table {table_number}")
        table = self._find_table(table_number)
        drink_not_in_menu = []
        drink = ''
        for name in drinks_name:
            drink = self._find_if_item_in_menu(name, self.drinks_menu)
            if drink:
                table.drink_orders.append(drink)
            else:
                drink_not_in_menu.append(name)
        result = f"Table {table_number} ordered:\n"
        x = len(table.drink_orders)
        for i in range(len(table.drink_orders)):
            # if not i == len(table.drink_orders) - 1:
            result += f"- {[drink.name for drink in table.drink_orders][i]} " \
                      f"{[drink.brand for drink in table.drink_orders][i]} - " \
                      f"{[drink.portion for drink in table.drink_orders][i]}ml - " \
                      f"{[drink.price for drink in table.drink_orders][i]}lv\n"
            # else:
            #     result += f"- {[drink.name for drink in table.drink_orders][i]} " \
            #               f"{[drink.brand for drink in table.drink_orders][i]} - " \
            #               f"{[drink.portion for drink in table.drink_orders][i]}ml - " \
            #               f"{[drink.price for drink in table.drink_orders][i]}lv"
        result += f'{self.name} does not have in the menu:\n'
        for i in range(len(drink_not_in_menu)):
            if not i == len(drink_not_in_menu) - 1:
                result += f'{[drink for drink in drink_not_in_menu][i]}\n'
            else:
                result += f'{[drink for drink in drink_not_in_menu][i]}'
        return result

    def leave_table(self, table_number):
        table = self._find_table(table_number)
        self.total_income += table.get_bill()
        table_bill = table.get_bill()
        table.clear()
        result = f"Table: {table_number}\n"
        result += f"Bill: {table_bill:.2f}lv."
        return result

    def get_free_tables_info(self):
        for table in self.table_repository:
            if not table.is_reserved:
                return table.free_table_info()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
