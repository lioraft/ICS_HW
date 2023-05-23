from unittest import TestCase
from RandomPlayer import RandomPlayer
from Hand import Hand
from Domino import Domino
from Player import Player


class TestPlayer(TestCase):
    """
    This class is an abstract class. therefore, an object of one of it's subclasses will be used
    in order to test the methods it inherits from Player.
    """
    def setUp(self):
        """
        setup for tests
        """
        self.p = RandomPlayer("lior", 23, Hand([Domino(2, 4), Domino(1, 2)]))

    def test_init(self):
        """
        Test for init
        """
        # If the object was made properly
        self.assertIsInstance(self.p, Player)
        self.assertIsInstance(self.p, RandomPlayer)
        # If the attributes were set properly
        self.assertEqual("lior", self.p.name)
        self.assertEqual(23, self.p.age)
        self.assertEqual(Hand([Domino(2, 4), Domino(1, 2)]), self.p.hand)

    def test_score(self):
        """
        Test for score
        """
        self.assertEqual(9, self.p.score())

    def test_has_dominoes(self):
        """
        Test for has_dominoes
        """
        self.assertTrue(self.p.has_dominoes())
        self.assertFalse(RandomPlayer("noa", 20, Hand([])).has_dominoes())

    def test_play(self):
        """
        abstract method that the subclass method overrides
        """
        pass

    def test_str(self):
        """
        Test for str
        """
        self.assertEqual("Name: lior, Age: 23, Hand: [2|4][1|2], Score: 9", str(self.p))

    def test_repr(self):
        """
        Test for repr
        """
        self.assertEqual("Name: lior, Age: 23, Hand: [2|4][1|2], Score: 9", repr(self.p))
