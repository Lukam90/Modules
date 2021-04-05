# coding: utf-8

import format

# 8) Compilation

# Liste des fichiers

def compileList(fileName):
    with open("build/" + fileName, "r") as fList:
        lines = fList.readlines()

        for line in lines:
            sFile = line.strip() # Nom de fichier

            if sFile != "" and line[0] != "#":
                format.markdownFile(sFile)
    
        fList.close()
    
    print("La liste %s a bien été compilée." % fileName)