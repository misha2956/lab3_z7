"""
This module contains all the funcitons and classes needed
for an object delivering interface.
"""
from typing import List

# store an available Order ID
next_available_ID = 10 ** 9

class Location:
    """
    Represents location of a delivery adress.
    """
    def __init__(self, city: str, postoffice: int):
        """
        Initialise the class with the given parameters.

        >>> location = Location("Lviv", 53)
        >>> location.city
        'Lviv'
        """
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Represents an Item one could buy in the store
    """
    def __init__(self, name: str, price: float):
        """
        This function initialises main attributes of an Item.

        >>> item = Item("Some Special Item", 200)
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        This function returns a string representaion of the Item.

        >>> item = Item("Some Special Item", 200)
        >>> len(item.__str__())
        32
        """
        return "\t" * 7 + f"{self.price} UAH\r{self.name}"


class Vehicle:
    """
    Represents a vehicle for delivering
    """
    def __init__(self, vehicleNo: int, isAvailable: bool=True):
        """
        This function initialises main attributes of a Vehicle.

        >>> vehicle = Vehicle(1)
        >>> vehicle.isAvailable
        True
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order:
    """
    Represents an order with all the needed info.
    """
    def __init__(
            self, user_name: str, city: str, postoffice: int,
            items: List[Item], vehicle: Vehicle=None
    ):
        """
        Initialise the class with the given parameters.

        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(
        ... user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        Your order number is 1000000003.
        """
        global next_available_ID
        self.orderId = next_available_ID
        next_available_ID += 1

        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle

        print(f"Your order number is {self.orderId}.")

    def __str__(self) -> str:
        """
        Returns a string representation of an order.

        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(
        ... user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        Your order number is 1000000004.
        >>> len(my_order.__str__())
        158
        """
        newline = '\n'
        return (
            f"ID: {self.orderId}\n" +
            f"Name: {self.user_name}\n" +
            f"Deliver To: {self.location}\n" +
            f"Delivery Vehicle: {self.vehicle}\n" +
            f"Items:\n{newline.join(str(item) for item in self.items)}\n"
        )

    def calculateAmount(self) -> float:
        """
        Calculate total price of the order.

        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(
        ... user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        Your order number is 1000000005.
        >>> print(my_order.calculateAmount())
        154
        """
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle: Vehicle):
        """
        This function assigns a Vehicle to an Order.
        """
        vehicle.isAvailable = False
        self.vehicle = vehicle


class LogisticSystem:
    """
    This class contains information about the
    user, one's order and transportation vehicles.
    """
    def __init__(self,
            vehicles: List[Vehicle], orders: List[Order]=[]
    ):
        """
        Initialise the class with the given parameters.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        """
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        This function is used to place an order.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(
        ... user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        Your order number is 1000000001.
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.placeOrder(my_order)
        There is no available vehicle to deliver an order.
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                available_vehicle = vehicle
                break
        else:
            print("There is no available vehicle to deliver an order.")
            return
        order.assignVehicle(available_vehicle)
        self.orders.append(order)

    def trackOrder(self, orderId: int) -> str:
        """
        This function is used to track the order.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order(
        ... user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        Your order number is 1000000002.
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.trackOrder(1000000000)
        Your order #1000000000 is sent to Lviv. Total price: 154 UAH.
        """
        order_obj = None
        for order in self.orders:
            if order.orderId == orderId:
                order_obj = order
                break
        else:
            print("No such order. (check the ID)")
            return
        print(
            f"Your order #{orderId} is sent to {order_obj.location.city}." +
            f" Total price: {order_obj.calculateAmount()} UAH."
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
