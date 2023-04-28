from project import Customer
from project import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
        return

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
        return

    def rent_dvd(self, customer_id: int, dvd_id: int):

        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in self.dvds:
                    if dvd_id == dvd.id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"
                        elif dvd.is_rented:
                            return "DVD is already rented"
                        elif customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                    customer.rented_dvds.append(dvd_id)
                    dvd.is_rented = True
                    return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in self.dvds:
                    if dvd_id == dvd.id:
                        if dvd in customer.rented_dvds:
                            customer.rented_dvds.remove(dvd_id)
                            dvd.is_rented = False
                            return f"{customer.name} has successfully returned {dvd.name}"
                        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join(self.customers) + '\n' + '\n'.join(self.dvds)

