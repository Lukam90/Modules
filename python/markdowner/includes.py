# 7) Includes

import format
import ranges

# Fichier

def includeFile(line):
    res = ""

    fileName = line.split("@include ")[1]

    if fileName[0] == "$": # Notes
        key = fileName.split("/")[0]
        folder = ranges.rangeFile(key)

        fileName = fileName.replace(key, folder)

    with open(fileName + ".md", 'r') as fTemp:
        lines = fTemp.readlines()

        for line in lines:
            res += format.markdownLine(line)
        
        fTemp.close()
    
    return res

# Script

def includeScript(line):
    source = line.split("@script ")[1]
    source = source.replace("$", "/public/js/")

    res = '<script src="%s.js"></script>\n' % source

    return res

# Composant

def includeComponent(line):
    composer = line.split("@")[1]

    with open("components/%s.html" % composer, "r") as fComponent:
        res = fComponent.read() + "\n"
        
        fComponent.close()

    return res