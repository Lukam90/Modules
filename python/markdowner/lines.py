# coding: utf-8

import re

import paragraphs

# 4) Lines

# Sauts de ligne

def addLineBreak(line):
    line = re.sub(r"&$", "<br>", line)

    return line

# Nouvelle ligne

def addNewLine(line):
    return paragraphs.makeTextBold(line)

# Ligne horizontale

def addHorizontalLine():
    return "<hr>\n"

# Ligne vide

def addBlankLine():
    return "\n"

# En-têtes

def makeHeader(line):
    level = line.count("#")
    title = line.split("# ")[1]

    headNumber = "h%s" % level

    start = "<" + headNumber + ">"
    end = "</" + headNumber + ">\n"

    header = start + title + end

    return header