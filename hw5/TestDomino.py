from unittest import TestCase
from Domino import Domino
import Exceptions


class TestDomino(TestCase):
    def setUp(self):
        """
        setup for the tests
        """
        self.d1 = Domino(4, 2)
        self.d2 = Domino(2, 4)

    def test_init(self):
        """
        Test for init
        """
        # Exception:
        # testing the right exception was raised for range of left side
        self.assertRaises(Exceptions.InvalidNumberException, Domino, -1, 5)
        # testing the right exception was raised for range of right side
        self.assertRaises(Exceptions.InvalidNumberException, Domino, 1, 7)
        # testing the right exception was raised for range of left side
        try:
            inavlid_domino = Domino(-1, 5)
        except Exceptions.InvalidNumberException as e:
            self.assertEqual(str(e), "ERROR Left side is not in the valid range!")
        # testing the right exception was raised for range of right side
        try:
            inavlid_domino = Domino(1, 7)
        except Exceptions.InvalidNumberException as e:
            self.assertEqual(str(e), "ERROR Right side is not in the valid range!")
        # If the object was made properly
        self.assertIsInstance(self.d1, Domino)
        # If the attributes were set properly
        self.assertEqual(4, self.d1.get_left())
        self.assertEqual(2, self.d1.get_right())

    def test_get_left(self):
        """
        Test for get_left
        """
        self.assertEqual(4, self.d1.get_left())

    def test_get_right(self):
        """
        Test for get_right
        """
        self.assertEqual(2, self.d1.get_right())

    def test_str(self):
        """
        Test for str
        """
        self.assertEqual("[4|2]", str(self.d1))

    def test_repr(self):
        """
        Test for repr
        """
        self.assertEqual("[4|2]", repr(self.d1))

    def test_eq(self):
        """
        Test for eq
        """
        # When objects are identical
        self.assertTrue(self.d1 == Domino(4, 2))
        # When flipped object is identical
        self.assertTrue(self.d2 == self.d1)
        # Objects are not equal
        self.assertFalse(self.d1 == Domino(1, 2))
        # Objects are not the same type
        self.assertFalse(self.d1 == ["not", "a", "domino"])

    def test_ne(self):
        """
        Test for ne
        """
        # When objects are identical
        self.assertFalse(self.d1 != (Domino(4, 2)))
        # When flipped object is identical
        self.assertFalse(self.d2 != self.d1)
        # Objects are not equal
        self.assertTrue(self.d1 != Domino(1, 2))
        # Objects are not the same type
        self.assertTrue(self.d1 != ["not", "a", "domino"])

    def test_gt(self):
        """
        Test for gt
        """
        # Sum is equal
        self.assertFalse(self.d1 > self.d2)
        # Sum is bigger
        self.assertTrue(self.d1 > Domino(1, 2))
        # Sum is smaller
        self.assertFalse(Domino(1, 2) > self.d1)
        # Objects are not the same type
        self.assertFalse(self.d1 > ["not", "a", "domino"])

    def test_contains(self):
        """
        Test for contains
        """
        self.assertTrue(2 in self.d1)
        self.assertFalse(3 in self.d1)

    def test_flip(self):
        """
        Test for flip
        """
        self.assertEqual(self.d1, self.d2.flip())
