prefix = {
    None: 1,
    "y": 1e-24, "yocto": 1e-24, # yocto
    "z": 1e-21, "zepto": 1e-21, # zepto
    "a": 1e-18, "atto": 1e-18, # atto
    "f": 1e-15, "femto": 1e-15, # femto
    "p": 1e-12, "pico": 1e-12, # pico
    "n": 1e-9, "nano": 1e-9, # nano
    "u": 1e-6, "micro": 1e-6, # micro
    "m": 1e-3,  "milli": 1e-3,# milli
    "c": 1e-2, "centi": 1e-2, # centi
    "d": 1e-1, "deci": 1e-1, # deci
    "da": 1e1, "deca": 1e1, # deca
    "h": 1e2, "hecto": 1e2, # hecto
    "k": 1e3, "kilo": 1e3, # kilo
    "M": 1e6, "mega": 1e6, # mega
    "G": 1e9, "giga": 1e9, # giga
    "T": 1e12, "tera": 1e12, # tera
    "P": 1e15, "peta": 1e15, # peta
    "E": 1e18, "exa": 1e18, # exa
    "Z": 1e21, "zetta": 1e21, # zetta
    "Y": 1e24, "yotta": 1e24, # yotta
    "Yi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Zi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Ei": 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Pi": 1024 * 1024 * 1024 * 1024 * 1024,
    "Ti": 1024 * 1024 * 1024 * 1024,
    "Gi": 1024 * 1024 * 1024,
    "Mi": 1024 * 1024,
    "Ki": 1024
}

binary_prefix = {
    "Yi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Zi": 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Ei": 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    "Pi": 1024 * 1024 * 1024 * 1024 * 1024,
    "Ti": 1024 * 1024 * 1024 * 1024,
    "Gi": 1024 * 1024 * 1024,
    "Mi": 1024 * 1024,
    "Ki": 1024
}



units = {
    ("meter", "feet"): 3.28,
    # ("meter", "foot"): 3.28

}


kwords = {
    "meter": None,
    "m": None,
    "inch": None,
    "in": None,
    "feet": None,
    "foot": None,
    "ft": None

}



"""
prefix = {
    None: 1,
    ("y", "yocto"): 1e-24,  # yocto
    ("z", "zepto"): 1e-21,  # zepto
    ("a", "atto"): 1e-18,  # atto
    ("f", "femto"): 1e-15,  # femto
    ("p", "pico"): 1e-12,  # pico
    ("n", "nano"): 1e-9,  # nano
    ("u", "micro"): 1e-6,  # micro
    ("m", "milli"): 1e-3,  # milli
    ("c", "centi"): 1e-2,  # centi
    ("d", "deci"): 1e-1,  # deci
    ("da", "deca"): 1e1,  # deca
    ("h", "hecto"): 1e2,  # hecto
    ("k", "kilo"): 1e3,  # kilo
    ("M", "mega"): 1e6,  # mega
    ("G", "giga"): 1e9,  # giga
    ("T", "tera"): 1e12,  # tera
    ("P", "peta"): 1e15,  # peta
    ("E", "exa"): 1e18,  # exa
    ("Z", "zetta"): 1e21,  # zetta
    ("Y", "yotta"): 1e24,  # yotta
}


alias = {
    "yocto": "y",
    "zepto": "z",
    "atto": "a",
    "femto": "f",
    "pico": "p",
    "nano": "n",
    "micro": "u",
    "milli": "m",
    "centi": "c",
    "deci": "d",
    "deca": "da",
    "hecto": "h",
    "kilo": "k",
    "mega": "M",
    "giga": "G",
    "tera": "T",
    "peta": "P",
    "exa": "E",
    "zetta": "Z",
    "yotta": "Y"
}

"""