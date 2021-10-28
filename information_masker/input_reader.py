"""Input Related Classes"""
from abc import abstractmethod


class InputReader:
    """
    Rest of application expects an consistent interface for input reading.
    """
    @abstractmethod
    def __init__(self):
        """Initializes input class. If necessary takes parameters"""
        raise NotImplementedError

    @abstractmethod
    def read_item(self):
        """Reads and returns single item from input source"""
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """Completes input"""
        raise NotImplementedError
