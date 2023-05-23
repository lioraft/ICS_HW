import Exceptions


class Domino:
    """
    A class that represents a domino piece.
    Attributes: left_side, right_side.
    """
    def __init__(self, left, right):
        """
        Constructor for Domino class.
        :param left: An integer. represents the left side of the domino piece.
        :param right: An integer. represents the right side of the domino piece.
        """
        if left < 0 or left > 6:
            raise Exceptions.InvalidNumberException("Left side is not in the valid range!")
        if right < 0 or right > 6:
            raise Exceptions.InvalidNumberException("Right side is not in the valid range!")
        self.__left_side = left
        self.__right_side = right

    def get_left(self):
        """
        :return: The value of the left side of the domino piece.
        """
        return self.__left_side

    def get_right(self):
        """
        :return: The value of the right side of the domino piece.
        """
        return self.__right_side

    def __str__(self):
        """
        :return: A string that contains the right and left sides of the domino piece.
        """
        return "[" + str(self.__left_side) + "|" + str(self.__right_side) + "]"

    def __repr__(self):
        """
        :return: A string that contains the right and left sides of the domino piece.
        """
        return str(self)

    def __eq__(self, other):
        """
        Takes in another object, returns if the two objects are not identical.
        :param other: An object.
        :return: A boolean: if the two objects are from the same type (Domino) and are identical,
        it will return True. otherwise, returns False.
        """
        if not isinstance(other, Domino):
            return False
        if self.__right_side == other.__right_side and self.__left_side == other.__left_side:
            return True
        if self.__right_side == other.__left_side and self.__left_side == other.__right_side:
            return True
        return False

    def __ne__(self, other):
        """
        Takes in another object, returns if the two objects are not identical.
        :param other: An object.
        :return: A boolean: if the two objects are from the same type (Domino) and are identical,
        it will return False. otherwise, returns True.
        """
        if (self == other) is True:
            return False
        return True

    def __gt__(self, other):
        """
        :param other: An object.
        :return: A boolean. If the sum of the sides of current domino piece is bigger than the sum of the
        sides of the other domino piece, returns True. otherwise, returns False.
        """
        if not isinstance(other, Domino):
            return False
        if self.__right_side + self.__left_side > other.__right_side + other.__left_side:
            return True
        return False

    def __contains__(self, key):
        """
        :param key: An integer.
        :return: A bool. if the domino piece contains key in one of its sides, returns True.
        otherwise, returns False.
        """
        if self.__right_side == key or self.__left_side == key:
            return True
        return False

    def flip(self):
        """
        :return: A flipped domino piece, meaning the left side of it is the right side of self and
        the right side of it is the left side of self.
        """
        flip_piece = Domino(self.__right_side, self.__left_side)
        return flip_piece
