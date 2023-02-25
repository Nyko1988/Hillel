#Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
class Vehicle:
    type_vehicle = "Cargo"
    maxim_speed = 100

    def __init__(self, type=type_vehicle, max_speed=maxim_speed):
        self.type = type
        self.max_speed = max_speed

    def start_engine(self):
        msg_start = f'{self.type_vehicle} is strted engine'
        return msg_start

    def stop_engine(self):
        msg_stop = f'{self.type_vehicle} is stopped engine'
        return msg_stop

class Car(Vehicle):
    number_of_wheels = 4
    transmissio_type = 'automatic'
    brand = 'Ford'

    def __init__(self,brand=brand, transmition=transmissio_type, wheels=number_of_wheels ):
        self. brand_of_vehicle = brand
        self.transmission = transmition
        self.wheels = wheels

    def presentation_of_car(self):
        msg_presentation = f'Car {self.brand_of_vehicle} has {self.transmission} transmision and {self.wheels} wheels.'
        return msg_presentation

class Plane(Vehicle):
    engines = 4
    fuel = 'reactive'

    def __init__(self, type=Vehicle.type_vehicle, number_of_engines = engines, fuel_type = fuel):
        self.type_of_plane = type
        self.number_of_engines = number_of_engines
        self.fuel_type = fuel_type

    def presentation_of_plane(self):
        msg_plane = f'{self.type_of_plane} planes have {self.number_of_engines} engines and use {self.fuel_type}'
        return msg_plane

class MotorBoat(Vehicle):
    type_of_engine = 'Motorboat'
    water_tonnage = 19

    def __init__(self, type=Vehicle.type_vehicle, max_speed = Vehicle.maxim_speed, type_of_engine=type_of_engine, tonage = water_tonnage):
        self.boat_type = type
        self.boat_speed = max_speed
        self.boat_type_engine = type_of_engine
        self.boat_tonage = tonage

    def presentation_of_boat(self):
        msg_boat = f'{self.boat_type} {self.boat_type_engine} has {self.boat_speed} km/h max speed and tonage is {self.boat_tonage}'
        return msg_boat


ford_car = Car()
print(ford_car.presentation_of_car())
mercedes_car = Car("Mercedes", 'mehanic', 8)
print(mercedes_car.presentation_of_car())

cargo_plane = Plane()
print(cargo_plane.presentation_of_plane())
passenger_plane = Plane('Passenger', 2, 'Cerosin')
print(passenger_plane.presentation_of_plane())

cargo_boat = MotorBoat()
print(cargo_boat.presentation_of_boat())
passenger_boat = MotorBoat("Passenger", 20, 'diselboat', 5)
print(passenger_boat.presentation_of_boat())