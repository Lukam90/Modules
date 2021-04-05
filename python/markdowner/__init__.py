# coding: utf-8

# Fichier de base du module

"""
1 - variables

Les variables globales du moteur Markdown

- buildLinks (liens de compilation)
- components (composants)
- table (mode tableau)
- long (mode paragraphe long)

2 - ranges

Les intervalles d'inclusion

- rangeFile (dossiers-intervalles des notes)

3 - paragraphs

Gestion des paragraphes

- addParagraph (ajout d'un nouveau paragraphe)
- toggleParagraph (début ou fin d'un paragraphe)
- makeTextBold (texte en gras)

4 - lines

- addLineBreak (ajout d'un saut de ligne)
- addNewLine (ajout d'une nouvelle ligne)
- addBlankLine (ajout d'un blanc ou ligne vide)
- makeHeader (ajout d'une en-tête)

5 - Tables

- addTableLine (ajout d'une ligne de tableau)
- startTable (début d'un tableau)
- endTable (fin d'un tableau)

6 - format

- markdownLine (formatage d'une ligne)
- markdownFile (formatage d'un fichier)

7 - includes

- includeFile (inclusion d'un fichier spécifique)
- includeScript (inclusion d'un script JS)
- includeComponent (inclusion d'un composant ou fichier de base)

8 - compilation

Compilation des fichiers

- compileList
"""