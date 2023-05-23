from unittest import TestCase
from RandomPlayer import RandomPlayer
from Hand import Hand
from Domino import Domino
from Board import Board
import copy
import random


class TestRandomPlayer(TestCase):
    def test_init(self):
        """
        Test for init
        """
        p = RandomPlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2)]))
        # If the object was made properly
        self.assertIsInstance(p, RandomPlayer)
        # If the attributes were set properly
        self.assertEqual("lior", p.name)
        self.assertEqual(23, p.age)
        self.assertEqual(Hand([Domino(2, 4), Domino(1, 2)]), p.hand)

    def test_play(self):
        """
        Test for play
        """
        p = RandomPlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2), Domino(1, 1)]))
        # A copy of the random hand
        random.seed(12)
        shuffled_hand = copy.deepcopy(p.hand)
        random.shuffle(shuffled_hand.array)
        b = Board(3)
        # Playing all the dominoes and testing they were added properly
        for i in range(0, 3):
            p.play(b)
            self.assertIn(b.array[i], shuffled_hand.get_collection())
        self.assertEqual(str(b), "[1|1][1|2][2|4]")
        # No more moves - board is full and no more dominoes
        self.assertFalse(p.play(b))
