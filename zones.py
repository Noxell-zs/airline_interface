"""Objects related to with seats on the plane.

Classes:
    Zone
        Assigning the reserve to a person.  Price calculation.
    Reserve
        Technical characteristics of plane.

"""


import random


class Zone:
    """Technical characteristics of plane.

    Methods:
        coefficient
            Setter and getter coefficient for calculating the price.

    Attributes:
        _seats - Int
            Total number of seats.
        __edge - Int
            edge of zones.
        first - Tuple
            tuple of first class.
        economy - Tuple
            tuple of economy class.
        business - Tuple
            tuple of business class.
        __coefficient - Float
            coefficient for calculating the price.
    """
    def __init__(self, seats):
        """Initialisation of zone.

        Attributes:
            seats - Int
                Total number of seats.
        """
        self._seats = seats
        self.__edge = self._seats // 14

        self.first = tuple(i for i in range(1, 7))
        self.economy = tuple(i for i in range(7, 6*self.__edge+1))
        self.business = tuple(i for i in range(6*self.__edge, self._seats+1))

        self.__coefficient = 1.0

    @property
    def coefficient(self):
        """Getter coefficient for calculating the price"""
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, num):
        """Setter coefficient for calculating the price"""
        if num in self.first:
            self.__coefficient = 2.9
        elif num in self.economy:
            self.__coefficient = 1.8
        else:
            self.__coefficient = 1.0

    def __str__(self):
        """String representation of all zones"""
        return (f'Первый класс, места 1-6 \n'
                f'Бизнес класс, места 7-{6*self.__edge} \n'
                f'Эконом класс, места {6 * self.__edge + 1}-{self._seats}')


class Reserve:
    """Technical characteristics of plane.

    Methods:
        take
            Reservation of seat.
        cancel
            Cancel of reservation.

    Attributes:
        seats - Int
            Total number of seats.
        free - List
            List of free seats.
    """

    def __init__(self, seats):
        """Initialisation of reservation.

        Attributes:
            seats - Int
                Total number of seats.
        """
        self.seats = seats
        self.free = [random.choice((0, 1, 1)) for _ in range(self.seats)]

    def __str__(self):
        """String representation of free seats."""
        _s = 'Свободные места'
        for i in range(6):
            _s += '\n'
            for j in range(self.seats // 6):
                _s += f'{j*6+i+1:03}  ' if self.free[j*6+i] else ' '*8
        return _s

    def take(self, num):
        """Reservation of seat.

        Attributes:
            num - Int
                current seat number.

        Return:
            Boolean
        """
        if 0 < num <= self.seats and self.free[num-1]:
            self.free[num-1] = 0
            return True
        return False

    def cancel(self, num):
        """Cancel of reservation.

        Attributes:
            num - Int
                current seat number.
        """
        if 0 < num <= self.seats:
            self.free[num-1] = 1