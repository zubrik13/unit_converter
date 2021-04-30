import sys
import argparse

from dict import prefix, units, si_units, kwords


class Inputs:
    """ Check if input is valid"""
    def split(self, arg_):
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

    def parse(self, inp):
        """
        Method to parse user input data into prefix and unit
        :param inp: user input; str
        :return: 2 arguments - prefix, unit; str
        """
        arg_ = self.split(inp)

        if arg_ is None:
            return False

        prefix = arg_[0]
        unit = arg_[1]

        return prefix, unit

    @staticmethod
    def alias(dict_, search_val):
        """
        Method looks for alias patterns stored in dictionary
        :param dict_: name of dictionary where supported patterns stored; dict
        :param search_val: pattern to look for; str
        :return: standardised output pattern if known; str or None
        """
        for key, val in dict_.items():
            if search_val in val:
                return key

    def is_valid(self, parser_out):
        """
        Method to check if input is valid
        :param parser_out: 2 arguments - prefix, unit
        :return: True or False
        """
        if len(parser_out[0]) == 0:
            return True
        else:
            prefix = self.alias(si_units, parser_out[0])

        if prefix is None:
            return False

        return True


class Parser:
    """ Split input into chunks"""
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
    @staticmethod
    def parser_(data):
        """
        Intermediate method to reduce a number of input arguments from Parser class
        by multiplication of amount and scale factor arguments:
        amount = num * (from_prefix / to_prefix)
        Output prefix argument is defined to be used in final output
        :param data: 5 arguments - amount, from_prefix, from_unit, to_prefix, to_unit; str
        :return: amount, from_unit, to_unit, out_prefix; str
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

    def result(self, data):
        """
        Method to trigger data conversion
        :param data: 5 arguments - amount, from_prefix, from_unit, to_prefix, to_unit; str
        :return: 2 arguments - conversion value, output unit; float, str
        """
        parse = self.parser_(data)
        self.convert_(parse)


def arg_check(arg_):
    """
    Method to validate input
    :param arg_: user input; str
    :return: True or False
    """
    split = Inputs().split(arg_)
    if split:
        parse = Inputs().parse(arg_)
    else:
        return False

    convert = Inputs().is_valid(parse)
    if convert:
        return True

    return False

if __name__ == "__main__":

    # Check No of arguments entered
    if len(sys.argv) > 4:
        print('You have specified too many arguments')
        sys.exit()

    # Add parser
    parser = argparse.ArgumentParser(description="Process conversion input data")

    parser.add_argument("Amount",
                        metavar="amount",
                        type=str,
                        help="amount to convert")

    parser.add_argument("Arg1",
                        metavar="from_unit",
                        type=str,
                        help="unit to convert from")

    parser.add_argument("Arg2",
                        metavar="to_unit",
                        type=str,
                        help="unit to convert to")

    args = parser.parse_args()

    amount = args.Amount
    arg1 = args.Arg1
    arg2 = args.Arg2

    # Check inputs
    if not amount.isdigit():
        print(f"Please enter an integer value, {amount} - is not an integer")
        sys.exit()

    if arg_check(arg1):
        pass
    else:
        print(f"Please enter valid unit {arg1} - is not supported")
        sys.exit()

    if arg_check(arg2):
        pass
    else:
        print(f"Please enter valid unit {arg2} - is not supported")
        sys.exit()

    input_str = f"{amount} {arg1} {arg2}"

    inp = Parser().parse_(input_str)
    Converter().result(inp)
