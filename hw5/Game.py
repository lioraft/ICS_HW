class Game:
    """
    A class that represents a Game.
    Attributes: board, team1, team2
    """
    def __init__(self, board, team1, team2):
        """
        A constructor for Game class.
        :param board: An object of type Board. It is the board of the game.
        :param team1: An object of type Team. It is the first team that will participate in the game.
        :param team2: An object of type Team. It is the second team that will participate in the game.
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        Returns which one of the teams of the game wins the game. it uses the board of the game,
        everytime a different team adds domino tiles to the board. the game finishes when one of the teams
        runs out of tiles or there are no more possible moves.
        """
        # Only when both of the teams has dominoes
        if self.team1.has_dominoes_team() and self.team2.has_dominoes_team():
            # If the first team can play and still has dominoes, the second team tries to make a move too and then
            # turn goes back to first team and so on.
            if self.team1.play(self.board):
                if self.team1.has_dominoes_team():
                    self.team2.play(self.board)
                    self.play()
            # Whenever the first team can't make a move, the second team tries to make a move.
            else:
                if self.team1.has_dominoes_team() and self.team2.play(self.board):
                    self.play()
        # If both teams ran out of moves or one of the teams played all their tiles, the result is printed
        if self.team1.score_team() < self.team2.score_team():
            return "Team " + self.team1.name + " wins Team " + self.team2.name
        elif self.team2.score_team() < self.team1.score_team():
            return "Team " + self.team2.name + " wins Team " + self.team1.name
        else:
            return "Draw!"
