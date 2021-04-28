from dict import prefix, units, kwords


class Parser:
    """ Split input into chunks to process"""

    # def __init__(self, converter: Converter):
    # def __init__(self, converter):
    #     self.converter = converter

    @staticmethod
    def split(arg_):

        for key in kwords.keys():
            try:
                if key != arg_[0]: # eliminate "m" match for "mega" prefix
                    if key in arg_:
                        arg_ = arg_.replace(key, "-" + key + "-")
                        return arg_
            except KeyError:
                print("This unit is not supported, please use either Distance or Data units.")

    def parse(self, inp):

        data = inp.lower().split()
        arg_1 = self.split(data[1])
        arg_2 = self.split(data[2])

        print(arg_1)
        print(arg_2)

        from_ = arg_1.split("-")
        to_ = arg_2.split("-")

        amount = data[0]
        if len(from_) > 1:
            from_prefix = from_[0]
            from_unit = from_[1]
        else:
            from_prefix = None
            from_unit = from_[0]

        if len(to_) > 1:
            to_prefix = to_[0]
            to_unit = to_[1]
        else:
            to_prefix = None
            to_unit = to_[0]

        return amount, from_prefix, from_unit, to_prefix, to_unit


class Converter:
    """ Units converter"""

    # def __init__(self, units, parent: Converter = None):
    #     self.units = units
    #     self.parent = parent
    @staticmethod
    def parser(data):

        # parse data
        num = int(data[0])
        from_prefix = prefix[data[1]]
        from_unit = data[2]
        to_prefix = prefix[data[3]]
        to_unit = data[4]

        si_factor = from_prefix / to_prefix
        amount = num * si_factor

        return amount, from_unit, to_unit

    @staticmethod
    def convert(parser_out):
        amount = parser_out[0]
        from_unit = parser_out[1]
        to_unit = parser_out[2]
        exp = (from_unit, to_unit)
        inv = (to_unit, from_unit)

        if exp in units:
            return print(f"{amount * units[exp]} {to_unit}")

        return None

    def supports(self, from_unit, to_unit):
        pattern = (from_unit, to_unit)
        if pattern in units:
            return True

        return False

    def result(self, data):
        parse = self.parser(data)
        self.convert(parse)


if __name__ == "__main__":
    # payload = "100 kmeTer nfEet"
    payload = "100 meTer fEet"

    # payload = "100 kilomeTer petafeet"
    # payload = "100 meTer fEet"

    inp = Parser().parse(payload)
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
