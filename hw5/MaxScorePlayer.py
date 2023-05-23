from Player import Player
from Board import Board
import copy


class MaxScorePlayer(Player):
    """
    A class that represents a max score player.
    Subclass of Player, has same attributes.
    """
    def __init__(self, name, age, hand):
        """
        A constructor for MaxScorePlayer class.
        :param name: str. The name of the max score player.
        :param age: int. The age of the max score player. it is between the values 0 - 120.
        :param hand: An object of type Hand. This object contains only objects of type Domino.
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
        Takes in a board, returns if the player can play by making the best valid scorable move.
        :param board: An object of type Board.
        :return: If the player can play - add a domino from his hand to the board, the function will
        return True. if not, the function returns False. The function tries to max the score a player can get
        by playing with the highest value domino tile.
        """
        # Sorting the hand and putting it in a deep copy so it won't sort the original hand as well.
        sorted_hand = copy.deepcopy(self.hand)
        if self.has_dominoes() and isinstance(board, Board):
            for i in range(0, len(sorted_hand)):
                for j in range(0, len(sorted_hand)-1):
                    if sorted_hand.array[j] > sorted_hand.array[j+1]:
                        temp_domino = sorted_hand.array[j]
                        sorted_hand.remove_domino(temp_domino)
                        sorted_hand.add(temp_domino, j+1)
        # Trying to make a move. first to the right side, and then to the left side.
        for i in range(0, len(sorted_hand)):
            if board.add_right(sorted_hand.array[len(sorted_hand)-1-i]):
                self.hand.remove_domino(sorted_hand.array[len(sorted_hand)-1-i])
                return True
            if board.add_left(sorted_hand.array[len(sorted_hand)-1-i]):
                self.hand.remove_domino(sorted_hand.array[len(sorted_hand)-1-i])
                return True
        return False

    def __str__(self):
        """
        :return: A string that contains all of the attributes of the object.
        """
        return Player.__str__(self) + ", I can win the game!"
