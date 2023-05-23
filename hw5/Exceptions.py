class EmptyBoardException(Exception):
    """
    An exception that will be raised when a board is empty.
    """
    pass


class FullBoardException(Exception):
    """
    An exception that will be raised when a board is full and can't contain more dominoes.
    """
    pass


class NoSuchDominoException(Exception):
    """
    An exception that will be raised when trying to remove a domino that isn't in the collection.
    """
    pass


class InvalidNumberException(Exception):
    """
    An exception that will be raised when trying to insert a number that isn't in the valid range.
    """
    def __init__(self, message):
        """
        Constructor for the exception.
        :param message: A message that will be raised when the exception occurs.
        """
        self.message = message

    def __str__(self):
        """
        :return: A string that contains the word "ERROR" and the message that should be raised
        when the exception occurs.
        """
        return 'ERROR ' + self.message
