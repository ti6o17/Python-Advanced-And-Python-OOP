from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)


    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)


    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_item_from_items(self.subscriptions, subscription_id)
        customer = self.__get_item_from_items(self.customers, subscription.customer_id)
        plan = self.__get_item_from_items(self.plans, subscription.exercise_id)
        equipment = self.__get_item_from_items(self.equipment, plan.equipment_id)
        trainer = self.__get_item_from_items(self.trainers, subscription.trainer_id)


        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(plan)

    @staticmethod
    def __get_item_from_items(items, item_id):
        for item in items:
            if item.id == item_id:
                return item


#