import random
from Player import Player
from Board import Board
import copy


class RandomPlayer(Player):
    """
    A class that represents a random player.
    Subclass of Player, has same attributes.
    """
    def __init__(self, name, age, hand):
        """
        A constructor for RandomPlayer class.
        :param name: str. The name of the random player.
        :param age: int. The age of the random player. it is between the values 0 - 120.
        :param hand: An object of type Hand. This object contains only objects of type Domino.
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        """
        Takes in a board, returns if the player can make a move or not.
        :param board: An object of type Board. 
        :return: If the player can play - add a domino from his hand (after it was shuffled) to the board,
        the function will return True. if not, the function returns False.
        """
        # Making a deep copy of the hand so the shuffle won't affect the original hand.
        shuffled_hand = copy.deepcopy(self.hand)
        random.shuffle(shuffled_hand.array)
        # Trying to add it to the right side first, and then to the left side.
        if self.has_dominoes() and isinstance(board, Board) and board.max_capacity > len(board):
            for i in range(0, len(shuffled_hand)):
                if board.add_right(shuffled_hand.array[i]):
                    self.hand.remove_domino(shuffled_hand.array[i])
                    return True
                if board.add_left(shuffled_hand.array[i]):
                    self.hand.remove_domino(shuffled_hand.array[i])
                    return True
        return False
