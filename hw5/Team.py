import copy


class Team:
    """
    A class that represents a Team.
    Attributes: name, players.
    """
    def __init__(self, name, players):
        """
        Constructor for Team class.
        :param name: str. the name of the team.
        :param players: List(Players). a list of objects of type Player.
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
        :return: A list of all the players of the team.
        """
        return copy.deepcopy(self.__players)

    def score_team(self):
        """
        :return: The score of all the players of the team.
        """
        total_score = 0
        for i in range(0, len(self.__players)):
            total_score = total_score + self.__players[i].score()
        return total_score

    def has_dominoes_team(self):
        """
        :return: If at least one of the players of the team has more dominoes in hand, the function
        returns True. otherwise, return False.
        """
        for i in range(0, len(self.__players)):
            if self.__players[i].has_dominoes():
                return True
        return False

    def play(self, board):
        """
        Takes in a board, returns if a player of the team can play a move or not.
        :param board: An object of type Board.
        :return: The function iterates the list in chronological order of appearance. if a player can
        play a move, it returns True. if not, returns False.
        """
        for i in range(0, len(self.__players)):
            if self.__players[i].play(board):
                return True
        return False

    def __str__(self):
        """
        :return: A string that contains all of the attributes of the object.
        """
        str_players = ""
        for i in range(0, len(self.__players)):
            str_players = str_players + " " + str(self.__players[i])
        return "Name " + self.name + ", Score team: " + str(self.score_team()) + ", Players:" + str_players

    def __repr__(self):
        """
        :return: A string that contains all of the attributes of the object.
        """
        return self.__str__()
