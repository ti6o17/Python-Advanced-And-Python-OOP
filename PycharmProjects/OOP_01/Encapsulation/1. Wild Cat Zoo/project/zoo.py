from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > 0:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__animal_capacity -= 1
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > 0:
            self.__workers_capacity -= 1
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for worker in self.workers:
            sum_salaries += worker.salary
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_animals = 0
        for animal in self.animals:
            tend_animals += animal.money_for_care
        if self.__budget >= tend_animals:
            self.__budget -= tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_numbers = 0
        lions = []
        cheetah_numbers = 0
        cheetahs = []
        tiger_numbers = 0
        tigers = []
        result = f"You have {len(self.animals)} animals"
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lion_numbers += 1
                lions.append(animal)
            if animal.__class__.__name__ == 'Cheetah':
                cheetah_numbers += 1
                cheetahs.append(animal)
            if animal.__class__.__name__ == 'Tiger':
                tiger_numbers += 1
                tigers.append(animal)
        result += f'\n' + f'----- {len(lions)} Lions:'
        for lion in lions:
            result += f'\n' + f'{lion}'
        result += f'\n' + f'----- {len(tigers)} Tigers:'
        for tiger in tigers:
            result += f'\n' + f'{tiger}'
        result += f'\n' + f'----- {len(cheetahs)} Cheetahs:'
        for cheetah in cheetahs:
            result += f'\n' + f'{cheetah}'
        return result

    def workers_status(self):
        keeper_numbers = 0
        keepers = []
        caretaker_numbers = 0
        caretakers = []
        vet_numbers = 0
        vets = []
        result = f"You have {len(self.workers)} workers"
        for worker in self.workers:
            if type(worker).__name__ == 'Keeper':
                keeper_numbers += 1
                keepers.append(worker)
            if type(worker).__name__ == 'Caretaker':
                caretaker_numbers += 1
                caretakers.append(worker)
            if type(worker).__name__ == 'Vet':
                vet_numbers += 1
                vets.append(worker)
        result += f'\n' + f'----- {len(keepers)} Keepers:'
        for keeper in keepers:
            result += f'\n' + f'{keeper}'
        result += f'\n' + f'----- {len(caretakers)} Caretakers:'
        for caretaker in caretakers:
            result += f'\n' + f'{caretaker}'
        result += f'\n' + f'----- {len(vets)} Vets:'
        for vet in vets:
            result += f'\n' + f'{vet}'


        return result


