# coding: utf-8

import vars

# 3) Paragraphs

# Ajout d'un paragraphe

def addParagraph(line):
    nb = len(line)

    line = line[1:nb]
    line = makeTextBold(line)

    return "<p>%s</p>\n" % line

# Début ou fin d'un paragraphe

def toggleParagraph():
    if vars.long:
        vars.long = False

        line = "</p>\n"
    else:
        vars.long = True

        line = "<p class='long'>\n"

    return line

# Texte en gras

def makeTextBold(line):
    line = line.replace("{", "<strong>")
    line = line.replace("}", "</strong>")

    return line