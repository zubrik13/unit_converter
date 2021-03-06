prefix = {
    None: 1,
    "nautical": 1.1507771465,
    # si
    "y": 1e-24, "yocto": 1e-24,
    "z": 1e-21, "zepto": 1e-21,
    "a": 1e-18, "atto": 1e-18,
    "f": 1e-15, "femto": 1e-15,
    "p": 1e-12, "pico": 1e-12,
    "n": 1e-9, "nano": 1e-9,
    "u": 1e-6, "micro": 1e-6,
    "m": 1e-3,  "milli": 1e-3,
    "c": 1e-2, "centi": 1e-2,
    "d": 1e-1, "deci": 1e-1,
    "da": 1e1, "deca": 1e1,
    "h": 1e2, "hecto": 1e2,
    "k": 1e3, "kilo": 1e3,
    "M": 1e6, "mega": 1e6,
    "G": 1e9, "giga": 1e9,
    "T": 1e12, "tera": 1e12,
    "P": 1e15, "peta": 1e15,
    "E": 1e18, "exa": 1e18,
    "Z": 1e21, "zetta": 1e21,
    "Y": 1e24, "yotta": 1e24,
    # binary
    "Yi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Zi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Ei": 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Pi": 1024 * 1024 * 1024 * 1024 * 1024,
    "Ti": 1024 * 1024 * 1024 * 1024,
    "Gi": 1024 * 1024 * 1024,
    "Mi": 1024 ** 2,
    "Ki": 1024
}

units = {
    # LENGTH
    ("meter", "meter"): 1,
    ("inch", "inch"): 1,
    ("foot", "foot"): 1,
    ("yard", "yard"): 1,
    ("rod", "rod"): 1,
    ("furlong", "furlong"): 1,
    ("mile", "mile"): 1,
    ("league", "league"): 1,
    # metric
    ("meter", "inch"): 39.37007874,
    ("meter", "feet"): 3.280839895,
    ("meter", "foot"): 3.280839895,
    ("meter", "yard"): 1.0936132983,
    ("meter", "rod"): 0.1988387815,
    ("meter", "furlong"): 0.0049709695,
    ("meter", "mile"): 0.0006213712,
    ("meter", "league"): 0.0002071233,
    # imperial
    ("inch", "foot"): 0.0833335,
    ("inch", "yard"): 0.0277778333,
    ("inch", "rod"): 0.0050505051,
    ("inch", "furlong"): 0.0001262626,
    ("inch", "mile"): 0.0000157829,
    ("inch", "league"): 0.0000052609,
    ("foot", "yard"): 0.333334,
    ("foot", "rod"): 0.0606060606,
    ("foot", "furlong"): 0.0015151515,
    ("foot", "mile"): 0.0001893936,
    ("foot", "league"): 0.0000631313,
    ("yard", "rod"): 0.1818181818,
    ("yard", "furlong"): 0.0045454455,
    ("yard", "mile"): 0.0005681807,
    ("yard", "league"): 0.0001893939,
    ("rod", "furlong"): 0.025,
    ("rod", "mile"): 0.0031249937,
    ("rod", "league"): 0.0010416667,
    ("furlong", "mile"): 0.12499975,
    ("furlong", "league"): 0.0416665833,
    ("mile", "league"): 0.3333333333,
    # DATA
    ("bit", "bit"): 1,
    ("byte", "byte"): 1,
    ("byte", "bit"): 8,
    # WEIGHTS
    ("gram", "gram"): 1,
    ("pound", "pound"): 1,
    ("gram", "pound"): 0.00220462,

}

# alias dictionary for units
kwords = {
    # LENGTH
    "inch": ["inch", "in"],
    "foot": ["foot", "feet", "ft"],
    "yard": ["yard", "yd"],
    "rod": ["rod", "rd"],
    "furlong": ["furlong", "fur"],
    "mile": ["mile", "mi"],
    "league": ["league", "lea"],
    "meter": ["meter"],
    # DATA
    "byte": ["byte", "B"],
    "bit": ["bit", "b"],
    # WEIGHTS
    "gram": ["gram"],
    "pound": ["pound"]
}

# alias dictionary for output prefix
si_units = {
    "yocto": ["yocto", "y"],
    "zepto": ["zepto", "z"],
    "atto": ["atto", "a"],
    "femto": ["femto", "f"],
    "pico": ["pico", "p"],
    "nano": ["nano", "n"],
    "micro": ["micro", "u"],
    "milli": ["milli", "m"],
    "centi": ["centi", "c"],
    "deci": ["deci", "d"],
    "deca": ["deca", "da"],
    "hecto": ["hecto", "h"],
    "kilo": ["kilo", "k", "Ki"],
    "mega": ["mega", "M", "Mi"],
    "giga": ["giga", "G", "Gi"],
    "tera": ["tera", "T", "Ti"],
    "peta": ["peta", "P", "Pi"],
    "exa": ["exa", "E", "Ei"],
    "zetta": ["zetta", "Z", "Zi"],
    "yotta": ["yotta", "Y", "Yi"]
}
