class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result

    def __str__(self):
        return f"Trainer <{self.id}> {self.name}"
