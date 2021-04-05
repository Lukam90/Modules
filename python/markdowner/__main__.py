# coding: utf-8

# Bibliothèques

import sys
import time

# Modules

import vars
import compilation

# Exécution

def __main__():
    # Source

    """
    if len(sys.argv) != 2:
        print("Format : python markdowner.py <mode>")
        exit()
    """

    mode = "p" #sys.argv[1]

    target = vars.buildLinks[mode]

    try:
        if target == "partial.txt":
            while True:
                compilation.compileList(target)

                time.sleep(15)
        else:
            compilation.compileList(target)
    except KeyboardInterrupt:
        print("\nFin du programme")

__main__()