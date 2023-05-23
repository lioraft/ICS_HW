from Player import Player
from Board import Board


class NaivePlayer(Player):
    """
    A class that represents a naive player.
    Subclass of Player, has same attributes.
    """
    def __init__(self, name, age, hand):
        """
        A constructor for NaivePlayer class.
        :param name: str. The name of the naive player.
        :param age: int. The age of the naive player. it is between the values 0 - 120.
        :param hand: An object of type Hand. This object contains only objects of type Domino.
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
        Takes in a board, returns if the player can make a move or not.
        :param board: An object of type Board.
        :return: If the player can play (add a domino from his hand to the board) the function
        will return True. if not, the function returns False.
        """
        if self.has_dominoes() and isinstance(board, Board) and board.max_capacity > len(board):
            for i in range(0, len(self.hand)):
                if board.add_right(self.hand.array[i]):
                    self.hand.remove_domino(self.hand.array[i])
                    return True
                if board.add_left(self.hand.array[i]):
                    self.hand.remove_domino(self.hand.array[i])
                    return True
        return False
