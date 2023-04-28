from project import client
from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __check_if_client_registered(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def __find_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def __check_if_meal_is_in_menu(self, meal_name: str):
        meal_name_list = []
        for meal in self.menu:
            meal_name_list.append(meal.name)
        if not meal_name in meal_name_list:
            raise Exception(f"{meal_name} is not on the menu!")
        return True

    def __check_if_meal_quantity_is_enough(self, meal_quantity, meal_name, meal_type):
        for meal in self.menu:
            if not meal.quantity >= meal_quantity:
                raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")
            return True

    def __clear_the_bill(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        client.shopping_cart = []
        client.bill = 0

    def register_client(self, phone_number: str):
        if self.__check_if_client_registered(phone_number):
            raise Exception("The client has already been registered!")
        new_client = Client(phone_number)
        self.clients_list.append(new_client)
        return f"Client {phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())
        return "\n".join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__validate_menu()
        if not self.__check_if_client_registered(client_phone_number):
            self.register_client(client_phone_number)

        client = self.__find_client(client_phone_number)
        current_meals_ordered = []
        current_bill = 0.0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if self.__check_if_meal_is_in_menu(meal_name):
                for meal in self.menu:
                    if meal.name == meal_name:
                        if self.__check_if_meal_quantity_is_enough(meal_quantity, meal_name, type(meal).__name__):
                            current_meals_ordered.append(meal_name)
                            current_bill += meal.price * meal_quantity
                            meal.quantity -= meal_quantity
                            client.ordered_meals_quantity[meal_name] = meal_quantity

        client.shopping_cart.extend(current_meals_ordered)
        client.bill += current_bill

        return f"Client {client_phone_number} successfully ordered {', '.join(client.shopping_cart)} for " \
               f"{client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        self.__clear_the_bill(client_phone_number)
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        self.receipt_id += 1
        result = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for " \
                 f"{client_phone_number}."
        self.__clear_the_bill(client_phone_number)
        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {self.receipt_id} clients."



