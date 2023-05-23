from unittest import TestCase
from MaxScorePlayer import MaxScorePlayer
from Hand import Hand
from Domino import Domino
from Board import Board


class TestMaxScorePlayer(TestCase):
    def test_init(self):
        """
        Test for init
        """
        p = MaxScorePlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2)]))
        # If the object was made properly
        self.assertIsInstance(p, MaxScorePlayer)
        # If the attributes were set properly
        self.assertEqual("lior", p.name)
        self.assertEqual(23, p.age)
        self.assertEqual(Hand([Domino(2, 4), Domino(1, 2)]), p.hand)

    def test_play(self):
        p = MaxScorePlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2), Domino(1, 1), Domino(5, 4), Domino(0, 0)]))
        b = Board(4)
        # Testing it took the tiles and played them from max score to min score
        p.play(b)
        self.assertEqual(str(b), "[5|4]")
        p.play(b)
        self.assertEqual(str(b), "[5|4][4|2]")
        p.play(b)
        self.assertEqual(str(b), "[5|4][4|2][2|1]")
        p.play(b)
        self.assertEqual(str(b), "[5|4][4|2][2|1][1|1]")
        # No more possible moves
        self.assertFalse(p.play(b))
        # Testing the dominoes were removed from the hand
        self.assertEqual(str(p.hand), "[0|0]")

    def test_str(self):
        """
        Test for str
        """
        p = MaxScorePlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2)]))
        self.assertEqual(str(p), "Name: lior, Age: 23, Hand: [2|4][1|2], Score: 9, I can win the game!")
