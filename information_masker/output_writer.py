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


class CvsWriter(OutputWriter):
    """
    Simple CVS backend for OutputWriter Class. Compatible with different separators
    """
    def __init__(self, filename=None, separator=","):
        self.__outfile = open(filename, "wt")
        self.__separator = separator

    def write_item(self, item):
        # line = self.__separator.join([str(x) for x in item]) + "\n"
        line = ""
        for i in item:
            line += str(i) + ", "
        line += "\n"
        self.__outfile.write(line)

    def close(self):
        self.__outfile.close()
