from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption \
                                # + self.INCREASE

    @abstractmethod
    def drive(self, distance):
       pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    INCREASE = 0.9

    def drive(self, distance):
        liters_need = distance * (self.fuel_consumption + self.INCREASE)
        if self.fuel_quantity >= liters_need:
            self.fuel_quantity -= liters_need

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    INCREASE = 1.6
    DECREASE = 0.95

    def drive(self, distance):
        liters_need = distance * (self.fuel_consumption + self.INCREASE)
        if self.fuel_quantity >= liters_need:
            self.fuel_quantity -= liters_need

    def refuel(self, fuel):
        self.fuel_quantity += (self.DECREASE * fuel)


#

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
