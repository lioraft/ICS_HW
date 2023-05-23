from unittest import TestCase
from Domino import Domino
from Hand import Hand
import Exceptions


class TestHand(TestCase):
    def setUp(self):
        """
        setup for the tests
        """
        self.h = Hand([Domino(2, 4), Domino(1, 2)])
        self.d = Domino(1, 2)

    def test_init(self):
        """
        Test for init
        """
        # If the object was made properly
        self.assertIsInstance(self.h, Hand)
        # If the attributes were set properly
        self.assertEqual([Domino(2, 4), Domino(1, 2)], self.h.array)

    def test_add(self):
        """
        Test for add
        """
        # When input doesn't include index
        self.h.add(self.d)
        self.assertEqual(Hand([Domino(2, 4), Domino(1, 2), self.d]), self.h)
        # When input includes index
        self.h.add(self.d, 1)
        self.assertEqual(Hand([Domino(2, 4), self.d, Domino(1, 2), self.d]), self.h)

    def test_remove_domino(self):
        """
        Test for remove_domino
        """
        # Removing a domino tile that exists in the hand
        self.assertEqual(1, self.h.remove_domino(self.d))
        # Exception - Removing a domino tile that doesn't exist in the hand:
        try:
            self.h.remove_domino(self.d)
        except Exceptions.NoSuchDominoException as e:
            # testing the right exception was raised
            self.assertIsInstance(e, Exceptions.NoSuchDominoException)
            # testing it displays the right message
            self.assertEqual(str(e), "Tile does not exist")

    def test_eq(self):
        """
        Test for eq
        """
        # Object is not of type Hand
        self.assertFalse(self.h == self.d)
        # Objects are identical
        self.assertTrue(Hand([Domino(2, 4), Domino(1, 2)]), self.h)
