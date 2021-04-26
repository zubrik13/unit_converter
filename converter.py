import re
from abc import ABCMeta, abstractmethod

from dict import prefix, units


class Parser:
    """ Split input into chunks to process"""

    # def __init__(self, converter: Converter):
    # def __init__(self, converter):
    #     self.converter = converter

    def parse(self, inp):
        # num = re.findall(r"\d+", inp)
        # units = re.findall(r"[a-z]+", inp.lower())

        data = inp.lower().split()
        from_ = data[1].split("-")
        to_ = data[2].split("-")

        # amount = num[0]
        amount = data[0]
        if len(from_) > 1:
            prefix_from = from_[0]
            unit_from = from_[1]
        else:
            prefix_from = None
            unit_from = from_[0]

        if len(to_) > 1:
            prefix_to = to_[0]
            unit_to = to_[1]
        else:
            prefix_to = None
            unit_to = to_[0]

        # prefix_from =
        # c_from = units[0]
        # prefix_to =
        # c_to = units[1]

        return amount, prefix_from, unit_from, prefix_to, unit_to


class Converter:
    """ Units converter"""

    # def __init__(self, units):
    #     self.units = units

    def convert(self, data):
        # print(data[0], data[1], data[2])
        global res

        # parse data
        amount = int(data[0])
        prefix_from = prefix[data[1]]
        unit_from = data[2]
        prefix_to = prefix[data[3]]
        unit_to = data[4]

        # print(amount, prefix_from, unit_from, prefix_to, unit_to)

        exp = (unit_from, unit_to)
        inv = (unit_to, unit_from)
        si_factor = prefix_from / prefix_to

        if exp in units:
            res = amount * units[exp] * si_factor

        return print(f"{res} {unit_to}")

if __name__ == "__main__":
    # payload = "100 k-meTer n-fEet"
    payload = "100 kilo-meTer mega-fEet"
    # payload = "100 meTer fEet"

    # test = prefix["Y"]
    # print(test)

    inp = Parser().parse(payload)
    # print(inp)
    r = Converter().convert(inp)
    # print(r)

    # num = re.findall(r'\d+', payload)
    # units = re.findall(r"[a-z]+", payload.lower())
    # print(num[0])
    # print(units)
    # print(type(num[0]))

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

"""
