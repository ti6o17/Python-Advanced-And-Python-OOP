from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = ''
        if not self.robots:
            return f"{self.name} Main Service:\nRobots: none"
        else:
            result += f"{self.name} Main Service:\nRobots: "
            result += f"{' '.join([r.name for r in self.robots])}\n"
        return result
