# coding: utf-8

import sys

from time import time, sleep
from links import *

# Composants

components = ["@header", "@end", "@footer"]

# Markdown > Lignes

def markdownLine(line):
    sLine = line.strip()
    nb = len(sLine)

    if line[0] == ":": # Paragraphe
        sLine = sLine[1:nb]

        return "<p>%s</p>\n" % sLine
    elif line != "": # Ligne
        return line
    else: # Blanc
        return "\n"

# Markdown > Fichier

def markdownFile(name):
    # Source

    with open(name + ".inc", 'r') as fSource:
        res = ""
        
        lines = fSource.readlines()

        for line in lines:
            sLine = line.strip()

            if line[0] == "@":
                if sLine.startswith("@include"): # Includes
                    fileName = sLine.split("@include ")[1]

                    if fileName[0] == "$":
                        fileName = fileName.replace("$", "notes/")

                    with open(fileName + ".inc", 'r') as fTemp:
                        lines = fTemp.readlines()

                        for line in lines:
                            res += markdownLine(line)
                        
                        fTemp.close()
                elif sLine.startswith("@list"): # List
                    title = sLine.split(" > ")[0]
                    table_id = sLine.split(" > ")[1]

                    title = title.replace("@list ", "")

                    res += '<button class="accordion">%s</button>\n' % title

                    res += '<div class="panel">\n'

                    res += '\t<table id="%s"></table>\n' % table_id

                    res += '</div>\n'
                elif sLine.startswith("@part"): # List
                    title = sLine.split(" > ")[0]
                    part_id = sLine.split(" > ")[1]

                    title = title.replace("@part ", "")

                    res += '<button class="accordion">%s</button>\n' % title

                    res += '<div class="panel">\n'

                    res += '\t<div id="part-%s"></div>\n' % part_id

                    res += '</div>\n'
                elif sLine.startswith("@script"): # Script (JS)
                    source = sLine.split("@script ")[1]
                    source = source.replace("$", "/public/js/")

                    res += '<script src="%s.js"></script>\n' % source
                elif sLine in components: # Composants
                    composer = sLine.split("@")[1]

                    with open("components/%s.html" % composer, "r") as fComponent:
                        res += fComponent.read() + "\n"
                        
                        fComponent.close()
            else:
                res += markdownLine(line)

        fSource.close()

        # Résultat

        with open(name + ".html", 'w') as fResult:
            print("Le fichier %s.html a bien été généré." % name)

            fResult.write(res)
            fResult.close()
    
    print("Le fichier %s.inc a bien été compilé." % name)

# Liste > Compilation

def compileList(fileName):
    with open("build/" + fileName, "r") as fList:
        lines = fList.readlines()

        for line in lines:
            sFile = line.strip()

            if sFile != "" and line[0] != "#":
                markdownFile(sFile)
    
        fList.close()
    
    print("La liste %s a bien été compilée." % fileName)

# Compilation

if len(sys.argv) != 2:
    print("Format : python markdowner.py <mode>")
    exit()

mode = sys.argv[1]

target = buildLinks[mode]

try:
    if target == "partial.txt":
        while True:
            compileList(target)

            sleep(15)
    else:
        compileList(target)
except KeyboardInterrupt:
    print("\nFin du programme")