from abc import ABC, abstractmethod


class Player(ABC):
    """
    An abstract class that represents a player.
    Attributes: name, age, hand.
    """
    def __init__(self, name, age, hand):
        """
        A constructor for Player class.
        :param name: str. The name of the player.
        :param age: int. The age of the player. it is between the values 0 - 120.
        :param hand: An object of type Hand. This object contains only objects of type Domino.
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        :return: The score of a player, which is the sum of the values of the domino tiles he has in hand.
        """
        current_score = 0
        for i in range(0, len(self.hand)):
            current_score = current_score + self.hand.array[i].get_left() + self.hand.array[i].get_right()
        return current_score

    def has_dominoes(self):
        """
        :return: A boolean: if the player has dominoes in hand, returns True. otherwise, returns False.
        """
        if self.hand.array == []:
            return False
        return True

    @abstractmethod
    def play(self, board):
        """
        An abstract method. this function is not implemented in this class.
        """
        pass

    def __str__(self):
        """
        :return: A string that contains all of the attributes of the object.
        """
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Hand: " + str(self.hand) + ", Score: " + str(self.score())

    def __repr__(self):
        """
        :return: A string that contains all of the attributes of the object.
        """
        return str(self)
