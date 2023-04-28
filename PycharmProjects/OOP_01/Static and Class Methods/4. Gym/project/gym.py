class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_item_from_items(self.subscriptions, subscription_id)
        customer = self.__get_item_from_items(self.customers, subscription.customer_id)
        plan = self.__get_item_from_items(self.plans, subscription.exercise_id)
        equipment = self.__get_item_from_items(self.equipment, plan.equipment_id)
        trainer = self.__get_item_from_items(self.trainers, subscription.trainer_id)

        return str(subscription) + '\n' + \
               str(customer) + '\n' + \
               str(trainer) + '\n' + \
               str(equipment) + '\n' + \
               str(plan)

    @staticmethod
    def __get_item_from_items(items, item_id):
        for item in items:
            if item.id == item_id:
                return item





