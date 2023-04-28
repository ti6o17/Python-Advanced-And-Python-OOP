class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        return f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([elem.name for elem in self.rented_dvds])})"

    # dvd_names joined by comma and space