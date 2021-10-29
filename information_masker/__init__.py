"""
InformationMasker
"""
from sys import argv
from .input_reader import CsvReader
from .output_writer import CsvWriter
from .statistics import SimpleStatistics
from .maskers import alpha_numeric_masker


def file_masker(infile):
    """
        Reads input file in such form: [ID, Name, Email, Billing, Location]
        Apply masks defined in maskers class.
        Writes output to masked_infile.cvs
        Two pass on input approach due to limit memory usage on very big input set
    """
    in_file, out_file = None, None
    try:
        # First pass to get Billing average, some statistics and error check
        header = ['ID', 'Name', 'Email', 'Billing', 'Location']
        in_file = CsvReader(infile, header)
        out_file = CsvWriter("masked_" + infile)
        stats = SimpleStatistics(["Name", "Billing"])

        for item in in_file:
            stats.process("Name", len(item[1]))
            stats.process("Billing", item[3])
        print("Name:", stats.column_info("Name"))
        print("Billing:", stats.column_info("Billing"))
        in_file.close()

        # Second Pass for output
        in_file = CsvReader(infile, header)
        out_file.write_item(header)
        for item in in_file:
            masked_item = (
                item[0],                        # ID
                alpha_numeric_masker(item[1]),  # Name
                alpha_numeric_masker(item[2]),  # Email
                stats.get_average("Billing"),      # Billing
                item[4]                         # Location
            )
            out_file.write_item(masked_item)
            # print(item, masked_item)

    except Exception as err:
        print("Application error:{} {}".format(err,type(err)))
    finally:
        if in_file:
            in_file.close()
        if out_file:
            out_file.close()


def main():
    """Main function for CLI"""
    if len(argv) <= 1:
        print("Argument missing")
        print("Usage: $ python3 -m InformationMasker customers.csv")
        return
    file_masker(argv[1])
