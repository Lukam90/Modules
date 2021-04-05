# coding: utf-8

import vars

import lines
import paragraphs
import tables
import includes

# 6) Format

# Ligne

def markdownLine(line):
    sLine = line.strip() # Suppression du saut de ligne

    if vars.table and sLine != "]": # Ajout d'une ligne de tableau
        line = tables.addTableLine(sLine)

    if vars.long and sLine != "%": # Saut de ligne (long paragraphe)
        line = lines.addLineBreak(line)

    if line[0] == ":": # Paragraphe
        line = paragraphs.addParagraph(sLine)
    elif line[0] == "#": # En-tête
        line = lines.makeHeader(sLine)
    elif sLine == "%": # Long paragraphe (avec sauts de ligne)
        line = paragraphs.toggleParagraph()
    elif sLine == "***": # Ligne horizontale
        line = lines.addHorizontalLine()
    elif sLine == "[": # Début de tableau
        line = tables.startTable()
    elif sLine == "]": # Fin de tableau
        line = tables.endTable()
    elif line != "": # Ligne (avec texte en gras)
        line = lines.addNewLine(line)
    else: # Blanc
        line = lines.addBlankLine()
    
    return line

# Fichier

def markdownFile(name):
    with open(name + ".md", 'r') as fSource:
        res = ""
        
        lines = fSource.readlines()

        for line in lines:
            sLine = line.strip()

            if line[0] == "@":
                if sLine.startswith("@include"): # Includes
                    res += includes.includeFile(sLine)
                elif sLine.startswith("@script"): # Script (JS)
                    res += includes.includeScript(sLine)
                elif sLine in vars.components: # Composants
                    res += includes.includeComponent(sLine)
            else:
                res += markdownLine(line)

        fSource.close()

        # Résultat

        with open(name + ".html", 'w') as fResult:
            print("Le fichier %s.html a bien été généré." % name)

            fResult.write(res)
            fResult.close()
    
    print("Le fichier %s.md a bien été compilé." % name)