from converter import Parser, Converter

test_cases = [
    # LENGTH
    "100 kmeter nfeet",
    "1 nauticalmile meter",
    "1 microleague millifoot",
    "13 dlea Mft",
    "1 ft fur",
    "100 kilometer dafeet",
    "1 ft m",
    "17 kilord Gin"
    # DATA
    "10 kbyte Mb",
    "8 bit byte",
    "100 GiB Mibit",
    "100 Gibit MiB"
    ]

if __name__ == "__main__":

    for item in test_cases:
        data = Parser().parse(item)
        print(Converter().result(data))
