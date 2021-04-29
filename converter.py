from dict import prefix, units, si_units, kwords


class Parser:
    """ Split input into chunks"""
    # def __init__(self, converter: Converter):
    # def __init__(self, converter):
    #     self.converter = converter

    @staticmethod
    def split_(arg_):
        """
        Static method to split input data into prefix (if exists) and unit based on known patterns stored
        in kwords dictionary
        :param arg_: user input; str
        :return: list containing prefix and unit; list of str
        """
        for key, val in kwords.items():
            try:
                for pattern in val:
                    if pattern in arg_:
                        arg_ = arg_.replace(pattern, "-" + pattern + "-")
                        arg_ = arg_.split("-")
                        return arg_
            except KeyError:
                print("This unit is not supported, please use either Distance or Data units.")

    def parse_(self, inp):
        """
        Method to parse user input data to make equation in general form:
        amount, prefix, initial unit, prefix, target unit
        :param inp: 3 arguments - amount, initial unit, target unit; str
        :return: 5 arguments - amount, prefix, initial unit, prefix, target unit; str
        """
        # parse initial data
        data = inp.split()
        arg_1 = self.split_(data[1])
        arg_2 = self.split_(data[2])

        amount = data[0]
        from_unit = arg_1[1]
        to_unit = arg_2[1]

        # check if prefix defined
        if len(arg_1[0]) == 0:
            from_prefix = None
        else:
            from_prefix = arg_1[0]

        if len(arg_2[0]) == 0:
            to_prefix = None
        else:
            to_prefix = arg_2[0]

        return amount, from_prefix, from_unit, to_prefix, to_unit


class Converter:
    """ Units converter"""
    # def __init__(self, units, parent: Converter = None):
    #     self.units = units
    #     self.parent = parent
    @staticmethod
    def parser_(data):
        """
        Intermediate method to reduce a number of input arguments from Parser class
        by multiplication of amount and scale factor arguments:
        amount = num * (from_prefix / to_prefix)
        Output prefix argument is defined to be used in final output
        :param data: 5 arguments - amount, from_prefix, from_unit, to_prefix, to_unit; str
        :return: amount, from_unit, to_unit, out_prefix; float, str, str, str
        """
        num = int(data[0])
        from_prefix = prefix[data[1]]
        from_unit = data[2]
        to_prefix = prefix[data[3]]
        out_prefix = data[3]
        to_unit = data[4]

        si_factor = from_prefix / to_prefix
        amount = num * si_factor

        if out_prefix is None:
            out_prefix = ""
        # print(out_prefix)

        return amount, from_unit, to_unit, out_prefix

    @staticmethod
    def alias_(dict_, search_val):
        """
        Method to ensure simplified syntax support.
        Looks for alias patterns stored in dictionary
        :param dict_: name of dictionary where supported patterns stored; dict
        :param search_val: pattern to look for; str
        :return: standardised output pattern; str
        """
        for key, val in dict_.items():
            if search_val in val:
                return key

    def convert_(self, parser_out):
        """
        Method to make final calculation of previously parsed data
        :param parser_out: 4 arguments - amount, from_unit, to_unit, out_prefix
        :return: 2 arguments - conversion value, output unit; float, str
        """
        amount = parser_out[0]
        from_unit = self.alias_(kwords, parser_out[1])
        to_unit = self.alias_(kwords, parser_out[2])
        to_prefix = self.alias_(si_units, parser_out[3])

        exp = (from_unit, to_unit)
        inv = (to_unit, from_unit)

        if to_prefix is None:
            to_prefix = ""

        if exp in units:
            return print(f"{amount * units[exp]:.7f} {to_prefix}{to_unit}")
        elif inv in units:
            return print(f"{amount / units[inv]:.7f} {to_prefix}{to_unit}")

        return None

    def supports(self, from_unit, to_unit):
        pattern = (from_unit, to_unit)
        if pattern in units:
            return True

        return False

    def result(self, data):
        """
        Method to trigger data conversion
        :param data: 5 arguments - amount, from_prefix, from_unit, to_prefix, to_unit; str
        :return: 2 arguments - conversion value, output unit; float, str
        """
        parse = self.parser_(data)
        self.convert_(parse)


if __name__ == "__main__":
    # payload = "100 kmeTer nfEet"
    # payload = "1 nauticalmile meter"
    # payload = "1 microleague millifoot"
    # payload = "1 ft fur"
    # payload = "100 kilometer dafeet"
    # payload = "1 ft m"
    # payload = "10 kbyte Mb"
    payload = "100 Mibit MiB"

    inp = Parser().parse_(payload)
    print(inp)
    Converter().result(inp)

"""
import os.path
import sys
import argparse

# Check No of arguments entered
if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

# Add parser
parser = argparse.ArgumentParser(description="Process DNA input data")

parser.add_argument("Path",
                    metavar='file_path',
                    type=str,
                    help='the path to list')

parser.add_argument("Length",
                    metavar="piece_length",
                    type=str,
                    help="the piece length")

args = parser.parse_args()

file_path = args.Path
l = args.Length

# Check if file exists
if not os.path.isfile(file_path):
    print("File does not exist. Please enter a valid file path")
    print("\n".join(os.listdir(file_path)))
    sys.exit()

# Check if input is digit
if not l.isdigit():
    print(f"Please enter an integer value, {l} - is not an integer")
    sys.exit()

L = int(l)

        # num = re.findall(r"\d+", inp)
        # units = re.findall(r"[a-z]+", inp.lower())



"""
