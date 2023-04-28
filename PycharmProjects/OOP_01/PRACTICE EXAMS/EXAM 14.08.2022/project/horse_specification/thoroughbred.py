from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    ADDITIONAL_SPEED = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        self.speed = min(self.speed + self.ADDITIONAL_SPEED, self.MAX_SPEED)