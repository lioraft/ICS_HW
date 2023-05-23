from unittest import TestCase
from Board import Board
from Domino import Domino
import Exceptions


class TestBoard(TestCase):
    def setUp(self):
        """
        setup for the tests
        """
        self.b = Board(3)
        self.d = Domino(1, 2)

    def test_init(self):
        """
        Test for init
        """
        # Exception: testing the right exception was raised
        self.assertRaises(Exceptions.InvalidNumberException, Board, -1)
        self.assertRaises(Exceptions.InvalidNumberException, Board, 42)
        # testing it displays the right message
        try:
            inavlid_board = Board(29)
        except Exceptions.InvalidNumberException as e:
            self.assertEqual(str(e), "ERROR Max capacity is out of the valid range!")
        # If the object was made properly
        self.assertIsInstance(self.b, Board)
        # If the attributes were set properly
        self.assertEqual(3, self.b.max_capacity)
        self.assertEqual([], self.b.array)

    def test_in_left(self):
        """
        Test for in_left
        """
        # Exception: when board is empty
        try:
            self.b.in_left()
        except Exceptions.EmptyBoardException as e:
            # testing the right exception was raised
            self.assertIsInstance(e, Exceptions.EmptyBoardException)
            # testing it displays the right message
            self.assertEqual(str(e), "Board is empty!")
        # When board has dominoes
        self.b.add(self.d)
        self.assertEqual(1, self.b.in_left())

    def test_in_right(self):
        """
        Test for in_right
        """
        # Exception: when board is empty
        try:
            self.b.in_right()
        except Exceptions.EmptyBoardException as e:
            # testing the right exception was raised
            self.assertIsInstance(e, Exceptions.EmptyBoardException)
            # testing it displays the right message
            self.assertEqual(str(e), "Board is empty!")
        # When board has dominoes
        self.b.add(self.d)
        self.assertEqual(2, self.b.in_right())

    def test_add_left(self):
        """
        Test for add_left
        """
        self.b.add(self.d)
        # Trying to add an object that isn't a domino
        self.assertFalse(self.b.add_left([5, 2]))
        # Adding is possible
        self.assertTrue(self.b.add_left(Domino(5, 1)))
        # Adding is possible when flipped
        self.assertTrue(self.b.add_left(Domino(5, 1)))
        # Adding is not possible
        self.assertFalse(self.b.add_left(Domino(3, 3)))
        # Trying to add when a board is full
        self.assertFalse(self.b.add_left(Domino(1, 5)))
        # Testing it added the objects properly
        self.assertEqual("[1|5][5|1][1|2]", str(self.b))

    def test_add_right(self):
        """
        Test for add_right
        """
        self.b.add(self.d)
        # Trying to add an object that isn't a domino
        self.assertFalse(self.b.add_right([5, 2]))
        # Adding is possible
        self.assertTrue(self.b.add_right(Domino(2, 5)))
        # Adding is possible when flipped
        self.assertTrue(self.b.add_right(Domino(2, 5)))
        # Adding is not possible
        self.assertFalse(self.b.add_right(Domino(3, 3)))
        # Trying to add when a board is full
        self.assertFalse(self.b.add_right(Domino(2, 5)))
        # Testing it added the objects properly
        self.assertEqual("[1|2][2|5][5|2]", str(self.b))

    def test_add(self):
        """
        Test for add
        """
        # Adding when a board is empty
        self.assertTrue(self.b.add(self.d))
        # Adding is not valid
        self.assertFalse(self.b.add(Domino(3, 3), False))
        # Adding to right side
        self.assertTrue(self.b.add(Domino(2, 2), True))
        # Adding to left side
        self.assertTrue(self.b.add(self.d, False))
        # Exception - Adding when a board is full
        with self.assertRaises(Exceptions.FullBoardException):
            self.b.add(Domino(2, 3))

    def test_eq(self):
        """
        Test for eq
        """
        b2 = Board(3)
        # Equal
        self.assertTrue(self.b == b2)
        # Not same type
        self.assertFalse(self.b == self.d)
        self.b.add(self.d)
        # Not equal
        self.assertFalse(self.b == b2)
