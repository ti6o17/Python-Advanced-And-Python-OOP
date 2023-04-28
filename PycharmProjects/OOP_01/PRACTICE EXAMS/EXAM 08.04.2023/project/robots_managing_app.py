from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {'MainService': MainService,
                           'SecondaryService': SecondaryService}
    VALID_ROBOT_TYPES = {'MaleRobot': MaleRobot,
                         'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception('Invalid service type!')
        self.services.append(self.VALID_SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        self.robots.append(self.VALID_ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def _return_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def _return_service(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._return_robot(robot_name)
        service = self._return_service(service_name)
        x = (type(robot) == MaleRobot and type(service))
        y = (type(robot) == FemaleRobot and type(service) == SecondaryService)
        if not((type(robot) == MaleRobot and type(service) == MainService)
               or (type(robot) == FemaleRobot and type(service) == SecondaryService)):
            return "Unsuitable service."
        if type(robot) == MaleRobot:
            if len([type(service) for service in self.services if type(service) == MainService]) >= MainService.CAPACITY:
                raise Exception("Not enough capacity for this robot!")

            self.robots.remove(robot)
            service.robots.append(robot)
        elif type(robot) == FemaleRobot:
            if len([type(service) for service in self.services if type(service) == SecondaryService]) >= SecondaryService.CAPACITY:
                raise Exception("Not enough capacity for this robot!")

            self.robots.remove(robot)
            service.robots.append(robot)
            return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._return_service(service_name)
        for robot in service.robots:
            if robot.name == robot_name:
                service.robots.remove(robot)
                self.robots.append(robot)
                return f"Successfully removed {robot_name} from {service_name}."
            raise Exception("No such robot in this service!")


    def feed_all_robots_from_service(self, service_name: str):
        service = self._return_service(service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self._return_service(service_name)
        service_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {service_price:.2f}."

    def __str__(self):
        result = ''
        for service in self.services:
            result += service.details()
        return result
            # x = [robot.details() for robot in service.robots]
            # result += f"{service.name} {type(service).__name__}:\n"
            # # result += f"Robots: {' '.join(robot.name for robot in service.robots)}\n"
            #
            # result += f"Robots: {' '.join([robot.details() for robot in service.robots])}\n"
        # return result

