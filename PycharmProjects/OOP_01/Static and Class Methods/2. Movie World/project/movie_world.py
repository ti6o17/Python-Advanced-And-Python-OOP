class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self,dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in self.dvds:
                    if dvd_id == dvd.id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"
                        if dvd.is_rented:
                            return "DVD is already rented"
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer_id == customer.id:
                for dvd in customer.rent_dvd:
                    if not dvd_id == dvd.id:
                        return f"{customer.name} does not have that DVD"
                    customer.rented_dvds.remove(dvd)
                    dvd.is_rented = False
                    return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customer_numbers = 0
        dvds_numbers = 0
        result = ''
        for customer in self.customers:
            customer_numbers += 1
            name_dvds = [dvd.name for dvd in customer.rented_dvds]
            result += f"{customer_numbers}: {customer.name} of age {customer.age}" \
                      f" has {len(customer.rented_dvds)} " \
                      f"rented DVD's ({', '.join(name_dvds)})\n"

        for dvd in self.dvds:
            dvds_numbers += 1
            y=dvd.creation_month
            # x = months_mapper[dvd.creation_month]
            result += f"{dvds_numbers}: {dvd.name} ({y} {dvd.creation_year}) " \
                      f"has age restriction {dvd.age_restriction}. Status: {dvd.if_rented()}\n"

        return result


    # def find_customer(self, customer_id):
    #     for customer_check in self.customers:
    #         if customer_check.id == customer_id:
    #             return customer_check