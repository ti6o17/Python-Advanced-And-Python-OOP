from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    ADDITIONAL_SPEED = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        self.speed = min(self.speed + self.ADDITIONAL_SPEED, self.MAX_SPEED)