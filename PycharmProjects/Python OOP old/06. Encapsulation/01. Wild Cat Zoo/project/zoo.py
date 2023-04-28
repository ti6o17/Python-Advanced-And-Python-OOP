from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend_expenses = 0
        for animal in self.animals:
            tend_expenses += animal.money_for_care
        if self.__budget < tend_expenses:
            return "You have no budget to tend the animal. They are unhappy."

        self.__budget -= tend_expenses
        return f"You tended all the animal. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = ''
        result += f"You have {len(self.animals)} animal\n"
        lions = []
        cheetahs = []
        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)

                for lion in lions:
                    result += f"----- {len(lions)} Lions\n"
                    result += repr(lion) + '\n'

            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)

                for cheetah in cheetahs:
                    result += f"----- {len(cheetahs)} Cheetah\n"
                    result += repr(cheetah) + '\n'
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)

                for tiger in tigers:
                    result += f"----- {len(tigers)} Tigers\n"
                    result += repr(tiger) + '\n'

        return result

    def workers_status(self):
        result = ''
        result += f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)

                for keeper in keepers:
                    result += f"----- {len(keepers)} Keepers\n"
                    result += repr(keeper) + '\n'

            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)

                for caretaker in caretakers:
                    result += f"----- {len(caretakers)} Caretaker\n"
                    result += repr(caretaker) + '\n'
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)

                for vet in vets:
                    result += f"----- {len(vets)} Vets\n"
                    result += repr(vet) + '\n'

        return result
