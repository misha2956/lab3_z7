"""
This module contains all the funcitons and classes needed
for an object delivering interface.
"""
from typing import List

class Location:
    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Represents an Item one could buy in the store
    """
    def __init__(self, name: str, price: float):
        """
        This function initialises main attributes of an Item.
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        This function returns a string representaion of the Item.

        >>> item = Item("Some Special Item", 200)
        >>> print(item)
        Some Special Item       				$200
        """
        return "\t" * 7 + f"${self.price}\r{self.name}"


class Vehicle:
    """
    Represents a vehicle for delivering
    """
    def __init__(self, vehicleNo: int, isAvailable: bool):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order:
    def __init__(
            self, orderId: int, user_name: str,
            location: Location, items: List[Item],
            vehicle: Vehicle=None
    ):
        """
        Initialise the class with the given parameters.
        """
        self.orderId = orderId
        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    def __str__(self) -> str:
        pass

    def calculateAmount(self) -> int:
        pass

    def assignVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle


class LogisticSystem:
    def __init__(self,
            orders: List[Order], vehicles: List[Vehicle]
    ):
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        pass

    def trackOrder(self, orderId: int) -> str:
        pass
