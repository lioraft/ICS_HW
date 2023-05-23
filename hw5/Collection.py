class Collection:
    """
    A class that represents a collection.
    Attributes: array.
    """
    def __init__(self, array):
        """
        Constructor for Collection class.
        :param array: A list of objects.
        """
        self.array = array

    def get_collection(self):
        """
        A getter function for collection class.
        :return: the attributes of the class (array).
        """
        return self.array

    def add(self, item, option):
        """
        A function that adds elements to the array.
        This function should be applied to each derived class differently, and therefore
        it is not going to be implemented in this class.
        """
        raise NotImplementedError("Can't be applied to this object!")

    def __len__(self):
        """
        :return: The length of the array of the object.
        """
        return len(self.array)

    def __getitem__(self, i):
        """
        Takes in an index, returns the element in that index from the array if possible.
        if not possible, returns None.
        """
        if i >= 0 and i < len(self):
            return self.array[i]
        return None

    def __eq__(self, other):
        """
        Takes in another object, returns if the two objects are identical.
        :param other: An object.
        :return: A boolean: if the two objects are from the type Collection and are identical,
        it will return True. otherwise, returns False.
        """
        if not isinstance(other, Collection):
            return False
        return self.array == other.array

    def __ne__(self, other):
        """
        Takes in another object, returns if the two objects are not identical.
        :param other: An object.
        :return: A boolean: if the two objects are from the type Collection and are identical,
        it will return False. otherwise, returns True.
        """
        if (self == other) is True:
            return False
        return True

    def __contains__(self, item):
        """
        Takes in an item, returns if the array of the object contains this item or not.
        :param item: An object.
        :return: A boolean: if the item is in the array, the function returns True.
        otherwise, returns False.
        """
        for i in range(0, len(self)):
            if self.array[i] == item:
                return True
        return False

    def __str__(self):
        """
        :return: A string that contains all of the elements in the array of the object.
        """
        col_str = ""
        for i in range(0, len(self)):
            col_str = col_str + str(self.array[i])
        return col_str

    def __repr__(self):
        """
        :return: A string that contains all of the elements in the array of the object.
        """
        return str(self)
