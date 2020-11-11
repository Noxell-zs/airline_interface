"""Objects related to technical characteristics.

Classes:
    Rate
        Assigning the reserve to a person.  Price calculation.
    Plane
        Technical characteristics of plane.

"""


import random


class Rate:
    """Assigning the reserve to a person.  Price calculation.

    Methods:
        price
            Setter and getter of price calculation.

    Attributes:
            place - Str
                Name of the destination.
            rate_name - Str
                Name of the rate.
            num - Int
                Number of seat.
            __price - Float
                Price of ticket.
    """

    def __init__(self, place, rate_name):
        """Initialisation of a rate.

        Attributes:
            place - Str
                Name of the destination
            rate_name - Str
                Name of the rate
        """
        self.place = place
        self.num = 0
        self.rate_name = rate_name
        self.__price = 0.0

    @property
    def price(self):
        """Getter of price calculation."""
        return self.__price

    @price.setter
    def price(self, k):
        """Setter of price calculation."""
        self.__price = (k * 7000.1 * (1.2 + 0.05 * len(self.place) +
                                      0.02 * len(self.rate_name)))


class Plane:
    """Technical characteristics of plane.

    Attributes:
        time - Str
            Name of the destination.
        flight - Int
            Number of flight.
        seats - Int
            Total number of seats.
    """

    def __init__(self):
        """Initialisation of a plane."""
        self.time = f'{random.randint(0,23):02}:{random.randint(0,59):02}'
        self.flight = random.randint(1, 1000)
        self.seats = 6 * random.randint(15, 25)

    def __str__(self):
        """String representation of flight number and arrival time"""
        return f'Номер рейса {self.flight}. Время прибытия {self.time}.'
