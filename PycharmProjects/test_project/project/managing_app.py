from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    VEHICLES_TYPES = {'PassengerCar': PassengerCar,
                      "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLES_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VEHICLES_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        route = Route(start_point, end_point, length, len(self.routes) + 1)

        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def _return_user(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user

    def _return_vehicle(self, license_plate_number):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def _return_route(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._return_user(driving_license_number)
        vehicle = self._return_vehicle(license_plate_number)
        route = self._return_route(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
            return str(vehicle)
        else:
            user.increase_rating()
            return str(vehicle)
        @prop

    def repair_vehicles(self, count: int):
        vehicle_to_repair = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                vehicle_to_repair.append(vehicle)
        sorted_vehicle_to_repair = sorted(vehicle_to_repair, key=lambda x: (x.brand, x.model))
        if count > len(vehicle_to_repair):
            count = len(vehicle_to_repair)
        for i in range(count):
            sorted_vehicle_to_repair[i].is_damaged = False
            sorted_vehicle_to_repair[i].recharge()

        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: x.rating, reverse=True)
        result = f"*** E-Drive-Rent ***\n"
        count = 0
        for user in sorted_users:
            count += 1
            if not count == len(sorted_users):
                result += f"{str(user)}\n"
            else:
                result += f"{str(user)}"
        return result
