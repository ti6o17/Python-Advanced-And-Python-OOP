class Cup:
    def __init__(self, size: int, quantity : int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

            return self.quantity
        return

    def status(self):
        status = self.size - self.quantity
        return status

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
