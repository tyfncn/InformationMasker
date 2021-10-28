"""
InformationMasker
"""
from sys import argv


def file_masker(infile):
    """
    Reads input file in such form: [ID, Name, Email, Billing, Location]
    Apply masks defined in maskers class.
    Writes output to masked_infile.cvs
    Two pass on input approach due to limit memory usage on very big input set
    """
    print(infile)


def main():
    """Main function for CLI"""
    if len(argv) <= 1:
        print("Argument missing")
        print("Usage: $ python3 -m InformationMasker customers.csv")
        return
    print("Usage: $ python3 -m InformationMasker customers.csv")
