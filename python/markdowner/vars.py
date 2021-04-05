# 1) Variables

# Codes

codes = {
    "EN" : "langues/EN",
    "EO" : "langues/EO",
    "DE" : "langues/DE",
    "ES" : "langues/ES",
    "HR" : "langues/HR",
    "HU" : "langues/HU",
    "IT" : "langues/IT",
    "JP" : "langues/JP",
    "KOR" : "langues/KOR",
    "PT" : "langues/PT",
    "SL" : "langues/SL",
    "ZH" : "langues/ZH"
}

# Intervalles

ranges = {
    # Notes

    "$N0" : "notes/1-100", # Index
    "$N1" : "1-100",
    "$N2" : "101-200",
    "$N3" : "201-300",
    "$N4" : "301-400",
    "$N5" : "401-500",
    "$N6" : "501-600",
    "$N7" : "601-700",
    "$N8" : "701-800",
    "$N9" : "801-900",
    "$N10" : "901-1000",

    # Langues

    "$ENB" : codes["EN"] + "/EN-Nombres",
    "$ENV" : codes["EN"] + "/EN-Vocabulaire",

    "$EON" : codes["EO"] + "/EO-Nombres",
    "$EOV" : codes["EO"] + "/EO-Vocabulaire",
    "$EOG" : codes["EO"] + "/EO-Grammaire",

    "$DEN" : codes["DE"] + "/DE-Nombres",
    "$DEL" : codes["DE"] + "/DE-Vocabulaire", # Lexique
    "$DEV" : codes["DE"] + "/DE-Verbes",

    "$ESN" : codes["ES"] + "/ES-Nombres",
    "$ESL" : codes["ES"] + "/ES-Vocabulaire", # Lexique
    "$ESV" : codes["ES"] + "/ES-Verbes",

    "$HRN" : codes["HR"] + "/HR-Nombres",

    "$HUN" : codes["HU"] + "/HU-Nombres",

    "$ITN" : codes["IT"] +"/IT-Nombres",
    "$ITL" : codes["IT"] +"/IT-Vocabulaire", # Lexique
    "$ITV" : codes["IT"] +"/IT-Verbes",

    "$JPK" : codes["JP"] + "/JP-Kanas",
    "$JPN" : codes["JP"] + "/JP-Nombres",

    "$KORH" : codes["KOR"] + "/KOR-Hangeul",

    "$PTN" : codes["PT"] + "/PT-Nombres",

    "$SLN" : codes["SL"] + "/SL-Nombres",

    "$ZHN" : codes["ZH"] + "/ZH-Nombres",

    # Pages

    "$about" : "pages/about",

    # Liens

    "$liens" : "data/liens"
}

# Liens

buildLinks = {
    "f" : "front.txt",
    "p" : "partial.txt",

    "N1" : "md-notes/1-100.txt",
    "N2" : "md-notes/101-200.txt",
    "N3" : "md-notes/201-300.txt",
    "N4" : "md-notes/301-400.txt",
    "N5" : "md-notes/401-500.txt",
    "N6" : "md-notes/501-600.txt",
    "N7" : "md-notes/601-700.txt",
    "N8" : "md-notes/701-800.txt",
    "N9" : "md-notes/801-900.txt",
    "N10" : "md-notes/901-1000.txt",

    "about" : "md-pages/about.txt",
    "newsletter" : "md-pages/newsletter.txt",

    "claviers" : "md-outils/claviers.txt",
    "editeurs" : "md-outils/editeurs.txt"
}

# Composants

components = ["@header", "@end", "@footer"]

# Modes

table = False # Tableau
long = False # Paragraphe