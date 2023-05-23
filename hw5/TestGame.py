from unittest import TestCase
from Game import Game
from Team import Team
from RandomPlayer import RandomPlayer
from NaivePlayer import NaivePlayer
from MaxScorePlayer import MaxScorePlayer
from Hand import Hand
from Domino import Domino
from Board import Board
from random import random

class TestGame(TestCase):
    def setUp(self):
        """
        Setup for the tests
        """
        center = MaxScorePlayer("Reynolds", 25, Hand([Domino(5, 6), Domino(4, 6)]))
        point_guard = NaivePlayer("Evans", 25, Hand([Domino(5, 3), Domino(2, 6)]))
        guard = NaivePlayer("Wilbekin", 25, Hand([Domino(4, 2), Domino(3, 4)]))
        self.maccabi = Team("Maccabi", [center, point_guard, guard])
        fc = NaivePlayer("Davis", 25, Hand([Domino(5, 3), Domino(1, 6)]))
        forward = MaxScorePlayer("Lebron", 25, Hand([Domino(6, 6), Domino(6, 6)]))
        point_guard2 = NaivePlayer("Westbrook", 25, Hand([Domino(1, 3), Domino(1, 2)]))
        self.lakers = Team("Lakers", [fc, forward, point_guard2])
        self.g = Game(Board(20), self.maccabi, self.lakers)

    def test_init(self):
        """
        Test for init
        """
        self.assertIsInstance(self.g, Game)
        self.assertIsInstance(self.g.board, Board)
        self.assertIsInstance(self.g.team1, Team)
        self.assertIsInstance(self.g.team2, Team)

    def test_play(self):
        """
        Test for play
        """
        # Team 2 wins
        self.assertEqual(self.g.play(), "Team Lakers wins Team Maccabi")
        # Team 1 wins
        bulls = Team("Bulls", [MaxScorePlayer("Jordan", 60, Hand([Domino(5, 3), Domino(4, 3)]))])
        g2 = Game(Board(2), self.lakers, bulls)
        self.assertEqual(g2.play(), "Team Lakers wins Team Bulls")
        # Draw
        g3 = Game(Board(5), self.maccabi, bulls)
        self.assertEqual(g3.play(), "Draw!")


