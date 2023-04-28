from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = ''
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"
        else:
            result += f"{self.name} Secondary Service:\nRobots: "
            result += f"{' '.join([r.name for r in self.robots])}\n"
        return result
