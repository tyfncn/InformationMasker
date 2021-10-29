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

    def __iter__(self):
        # needed to run reading function as part of loop
        return self

    def __next__(self):
        # needed to run reading function as part of loop
        buffer = self.read_item()
        if not buffer:
            raise StopIteration
        else:
            return buffer


class CsvReader(InputReader):
    """
    Simple CVS backend for InputReader Class. Compatible with different separators
    """
    def __init__(self, filename=None, header=None, separator=","):
        # Open and check CVS file
        self.__infile = open(filename, "rt")
        self.__separator = separator
        self.__header = header
        assert header is not None, "CVS header needed"
        file_header = self.read_item()
        assert file_header == header, "Input file header error.\n" \
                                      "Expected:{}\nFound:{}".format(header, file_header)

    def read_item(self):
        """ Read input file and return parsed columns as list"""
        line = self.__infile.readline()
        if not line:
            return None

        formatted_line = self.parse_items(line)
        assert len(formatted_line) >= len(self.__header), "column count error:" \
                                                          "{}".format(formatted_line)
        return formatted_line

    def parse_items(self, line_value):
        """ split line into array items based on separator given in class constructor"""
        result = []
        parsed_column = ""
        for single_char in line_value:
            if single_char == self.__separator:
                result.append(self.guess_type(parsed_column))
                parsed_column = ""
            else:
                parsed_column += single_char
        if len(parsed_column) > 0:
            result.append(self.guess_type(parsed_column))
        return result

    @staticmethod
    def guess_type(value):
        """In CVS everything is string. This functions tries to guess type from string
         in simple terms."""
        result = value.strip()  # as string
        try:
            result = float(value)
            if result.is_integer():
                result = int(result)
        except ValueError:
            pass
        return result

    def close(self):
        self.__infile.close()
