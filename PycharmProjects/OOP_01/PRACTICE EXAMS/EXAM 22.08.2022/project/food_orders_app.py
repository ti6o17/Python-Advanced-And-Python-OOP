from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.client_list = []

    # @staticmethod
    # def __unpack_item_name_and_quantity(names_and_quantities):
    #     list_meal_names = []
    #     list_
    #     for meal_name, quantity in names_and_quantities:
    #         self.(meal_name)
    #         return name, quantity
    @classmethod
    def __increase_receipt_id(cls):
        FoodOrdersApp.RECEIPT_ID += 1
        return FoodOrdersApp.RECEIPT_ID

    def __find_client_by_phone_number(self, phone_number):
        for client in self.client_list:
            if client.phone_number == phone_number:
                return client

    def __check_if_meal_in_menu(self, meal_name):
        count = 0
        for meal in self.menu:
            if meal.name == meal_name:
                count += 1
        if count == 0:
            raise Exception(f"{meal_name} is not on the menu!")
        return

    def __check_if_enough_quantity_of_meal(self, meal_names_and_quantities):
        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                meals_corrected = ["Starter", "MainDish", "Dessert"]
                x = meal.__class__.__name__
                if x in meals_corrected:
                    if meal.quantity >= quantity:
                        continue
                    else:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
        return

    @staticmethod
    def __if_correct_meal(*meals):
        meals_corrected = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            x = meal[1].__class__.__name__
            if meal[1].__class__.__name__ in meals_corrected:
                return True

    def register_client(self, client_phone_number: str):
        for client in self.client_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.client_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if self.__if_correct_meal(meals):
                self.menu.append(meal)

    def show_menu(self):
        result = ''
        count = 0
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        for meal in self.menu:
            if count == 0:
                count += 1
                result += f'{meal.details()}'
            else:
                result += f'\n{meal.details()}'

        return result

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        if self.__find_client_by_phone_number(client_phone_number) is None:
            self.register_client(client_phone_number)
        else:
            client = self.__find_client_by_phone_number(client_phone_number)
        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if self.__check_if_enough_quantity_of_meal(meal_names_and_quantities) is None:
                        if self.__check_if_meal_in_menu(meal_name) is None:

                            client.shopping_cart.append(meal)
                            client.bill += quantity * meal.price
                            meal.quantity -= quantity
                            x = self.client_list
                            meals_list = [z.shopping_cart for z in self.client_list][0]
                            meals_names = [meal.name for meal in meals_list]
        return f"Client {client_phone_number} successfully ordered {', '.join(meals_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for client_meal in client.shopping_cart:
            for menu_meal in self.menu:
                if client_meal.name == menu_meal.name:
                    menu_meal.quantity += client_meal.quantity

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        id_receipt = FoodOrdersApp.__increase_receipt_id()
        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        return f"Receipt #{id_receipt} with total amount of " \
               f"{total_paid_money:.2f} was successfully paid for " \
               f"{client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.client_list)} clients."





