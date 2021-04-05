# coding: utf-8

# 5) Tables

import vars

# Ligne de tableau

def addTableLine(line):
    start = "<tr>\n"
    start += "<td>"

    line = line.replace(";", "</td>\n<td>")
    line = line.replace("&", "<br>")

    end = "</td>\n"
    end += "</tr>\n"

    line = start + line + end

    return line

# Début de tableau

def startTable():
    vars.table = True

    return "<table>\n"

# Fin de tableau

def endTable():
    vars.table = False

    return "</table>\n"