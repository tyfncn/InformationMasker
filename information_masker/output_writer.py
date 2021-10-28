"""Output related classes"""
from abc import abstractmethod


class OutputWriter:
    """
    Rest of application expects an consistent interface for output writing.
    """
    @abstractmethod
    def __init__(self):
        """Initializes input class. If necessary takes input parameters"""
        raise NotImplementedError

    @abstractmethod
    def write_item(self, item):
        """Takes item as parameter and writes it to output target"""
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """Completes input"""
        raise NotImplementedError
