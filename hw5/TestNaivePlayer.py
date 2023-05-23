from unittest import TestCase
from NaivePlayer import NaivePlayer
from Hand import Hand
from Domino import Domino
from Board import Board


class TestNaivePlayer(TestCase):
    def test_init(self):
        """
        Test for init
        """
        p = NaivePlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2)]))
        # If the object was made properly
        self.assertIsInstance(p, NaivePlayer)
        # If the attributes were set properly
        self.assertEqual("lior", p.name)
        self.assertEqual(23, p.age)
        self.assertEqual(Hand([Domino(2, 4), Domino(1, 2)]), p.hand)

    def test_play(self):
        """
        Test for play
        """
        p = NaivePlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2), Domino(1, 1)]))
        b = Board(3)
        b.add(Domino(2, 2))
        # Playing to the right side of the board
        self.assertTrue(p.play(b))
        # Testing the domino was added to the board
        self.assertEqual("[2|2][2|4]", str(b))
        # Testing the domino was removed from the hand of the player
        self.assertEqual("[1|2][1|1]", str(p.hand))
        # Playing to the left side of the board
        self.assertTrue(p.play(b))
        # Testing the domino was added to the board
        self.assertEqual("[1|2][2|2][2|4]", str(b))
        # Testing the domino was removed from the hand of the player
        self.assertEqual("[1|1]", str(p.hand))
        # Trying to play when a board is full
        self.assertFalse(p.play(b))
