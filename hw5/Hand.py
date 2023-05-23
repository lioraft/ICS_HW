from Collection import Collection
import Exceptions


class Hand(Collection):
    """
    A class that represents a hand.
    Subclass of Collection.
    Attributes: dominoes.
    """
    def __init__(self, dominoes):
        """
        Constructor for hand class.
        :param dominoes: A list of objects of domino type.
        """
        Collection.__init__(self, dominoes)

    def add(self, domino, index=None):
        """
        Takes in a domino and adds it to the Hand.
        :param domino: An object of type domino.
        :param index: An index. Default value is None. if not none, should be of type int.
        :return: If the index is none, the function will append domino
        to the end of the list. otherwise, it will insert it in the index position.
        """
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        """
        :param domino: An object of type domino.
        :return: (int/Exception): if the hand contains the object, the function removes
        it and returns the index it was in. if not, the function raises exception.
        """
        if domino in self:
            index = self.array.index(domino)
            self.array.remove(domino)
            return index
        raise Exceptions.NoSuchDominoException("Tile does not exist")

    def __eq__(self, other):
        """
        Takes in another object, returns if the two objects are identical.
        :param other: An object.
        :return: A boolean: if the two objects are from the type Hand and are identical,
        it will return True. otherwise, returns False.
        """
        if not isinstance(other, Hand):
            return False
        return self.array == other.array
