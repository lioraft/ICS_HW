from Collection import Collection
import Exceptions
from Domino import Domino


class Board(Collection):
    """
    A class that represents a board.
    Subclass of Collection.
    Attributes: max_capacity, array.
    """
    def __init__(self, max_capacity):
        """
        Constructor for board class.
        :param max_capacity: the max capacity of domino objects a board can contain.
        """
        if max_capacity < 1 or max_capacity > 28:
            raise Exceptions.InvalidNumberException("Max capacity is out of the valid range!")
        Collection.__init__(self, [])
        self.max_capacity = max_capacity

    def in_left(self):
        """
        :return: The leftest value in the board. if the board is empty, exception will be raised.
        """
        if self.array == []:
            raise Exceptions.EmptyBoardException("Board is empty!")
        return self.array[0].get_left()

    def in_right(self):
        """
        :return: The rightest value in the board. if the board is empty, exception will be raised.
        """
        if self.array == []:
            raise Exceptions.EmptyBoardException("Board is empty!")
        return self.array[len(self)-1].get_right()

    def add_left(self, domino):
        """
        Takes in a new domino object, and tries to add it to the left side of the board. if possible,
        returns True. otherwise, returns False.
        :param domino: An object of the type Domino.
        :return: boolean: if the board didn't reach it's full capacity and can hold more dominos, and the values of the
        domino matches the domino on the left, the domino will be inserted and the function returns True.
        if not possible to add, the function returns False.
        """
        if not isinstance(domino, Domino):
            return False
        if len(self) == self.max_capacity:
            return False
        if self.array == []:
            self.array.append(domino)
            return True
        if self.in_left() == domino.get_right():
            self.array.insert(0, domino)
            return True
        newdomino = domino.flip()
        if self.in_left() == newdomino.get_right():
            self.array.insert(0, newdomino)
            return True
        return False

    def add_right(self, domino):
        """
        Takes in a new domino object, and tries to add it to the right side of the board. if possible,
        returns True. otherwise, returns False.
        :param domino: An object of the type Domino.
        :return: boolean: if the board didn't reach it's full capacity and can hold more dominos, and the values of the
        domino matches the domino on the right, the domino will be inserted and the function returns True.
        if not possible to add, the function returns False.
        """
        if not isinstance(domino, Domino):
            return False
        if len(self) == self.max_capacity:
            return False
        if self.array == []:
            self.array.append(domino)
            return True
        if self.in_right() == domino.get_left():
            self.array.append(domino)
            return True
        newdomino = domino.flip()
        if self.in_right() == newdomino.get_left():
            self.array.append(newdomino)
            return True
        return False

    def add(self, domino, add_to_right=True):
        """
        Takes in a new domino object and a boolean that represents a side of the board, and tries to add
        it to the board. if possible, returns True. otherwise, returns False.
        :param domino: An object of the type Domino.
        :param add_to_right: If true, the function will try to insert to the right side of the board.
        if false, the function will try to insert to the left side of the board.
        :return: boolean/Exception: if the board reach it's full capacity and can't hold more dominos,
        the function will raise an exception. if the board is not full and the values of the
        domino matches one of the values on the sides, the domino will be inserted and the function returns True.
        if not possible to add, the function returns False.
        """
        if len(self) == self.max_capacity:
            raise Exceptions.FullBoardException("Board is full!")
        if add_to_right is True and self.add_right(domino) is True:
            return True
        if add_to_right is False and self.add_left(domino) is True:
            return True
        return False

    def __eq__(self, other):
        """
        Takes in another Board, returns if the boards are equal or not.
        :param other: An object of type board.
        :return: boolean: if the two boards are equal, the function returns True. otherwise, returns False.
        """
        if not isinstance(other, Board):
            return False
        if self.max_capacity == other.max_capacity and self.array == other.array:
            return True
        return False
