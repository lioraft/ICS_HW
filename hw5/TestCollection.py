from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def setUp(self):
        """
        setup for the tests
        """
        self.col = Collection([1, 3, 7, 9, 13, 15])

    def test_init(self):
        """
        Test for init
        """
        # If the object was made properly
        self.assertIsInstance(self.col, Collection)
        # If the attributes were set properly
        self.assertEqual([1, 3, 7, 9, 13, 15], self.col.array)

    def test_get_collection(self):
        """
        Test for get_collection
        """
        self.assertEqual([1, 3, 7, 9, 13, 15], self.col.get_collection())

    def test_add(self):
        """
        Test for add
        """
        try:
            self.col.add(21, 25)
        except NotImplementedError as e:
            # Exception: testing the right exception was raised
            self.assertIsInstance(e, NotImplementedError)
            # testing it displays the right message
            self.assertEqual(str(e), "Can't be applied to this object!")

    def test_getitem(self):
        """
        Test for getitem
        """
        col2 = Collection(["a", True, 42])
        self.assertEqual(1, self.col[0])
        self.assertEqual(True, col2[1])
        # Index is out of range
        self.assertEqual(None, col2[5])

    def test_eq(self):
        """
        Test for eq
        """
        col2 = Collection([1, 3, 7, 9, 13, 15])
        col3 = Collection(["a", True, 42])
        lst = ["not", "a", "collection"]
        # Equal
        self.assertTrue(self.col == col2)
        # Not equal
        self.assertFalse(self.col == col3)
        # Not same type
        self.assertFalse(self.col == lst)

    def test_ne(self):
        """
        Test for ne
        """
        col2 = Collection([1, 3, 7, 9, 13, 15])
        col3 = Collection(["a", True, 42])
        lst = ["not", "a", "collection"]
        # Equal
        self.assertFalse(self.col != col2)
        # Not equal
        self.assertTrue(self.col != col3)
        # Not same type
        self.assertTrue(self.col != lst)

    def test_len(self):
        """
        Test for len
        """
        self.assertEqual(6, len(self.col))

    def test_contains(self):
        """
        Test for contains
        """
        self.assertTrue(7 in self.col)
        self.assertFalse(21 in self.col)

    def test_str(self):
        """
        Test for str
        """
        self.assertEqual("13791315", str(self.col))

    def test_repr(self):
        """
        Test for repr
        """
        self.assertEqual("13791315", repr(self.col))
