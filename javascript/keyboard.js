/* Variables */

const tabLines = document.getElementById("lines");
const tabChars = document.getElementById("chars");

const result = document.getElementById("result");

const fileName = document.getElementById("filename");
const extension = document.getElementById("extension");

let csvChars = [];

/* Fonctions */

// Accordéon

function toggleLink() {
    var charsList = document.getElementById("chars-list");

    if (charsList.style.display == "block") charsList.style.display = "none";
    else charsList.style.display = "block";
}

// Conversion

function convertText() {
    let text = tabLines.value;

    for (const el in csvChars) {
        const obj = csvChars[el];

        text = text.replace(new RegExp(obj.key, "g"), obj.char);
    }

    result.value = text;
}

// Téléchargement

function downloadFile(filename, text) {
    let element = document.createElement("a");
    element.setAttribute(
        "href",
        "data:text/plain;charset=utf-8," + encodeURIComponent(text)
    );
    element.setAttribute("download", filename);

    element.style.display = "none";

    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

// Sauvegarde

function saveText() {
    const fSave = fileName.value + "." + extension.value;

    convertText();

    const fText = result.value;

    downloadFile(fSave, fText);
}

// Caractères > Tableau

async function fetchChars(code) {
    const response = await fetch(`chars/${code}.csv`);

    const text = await response.text();

    const lines = text.split("\n");

    for (let el of lines) {
        let line = el.split(";");

        let key = line[0];
        let char = line[1];

        let children = "";

        children += "<tr>";

        // Char

        if (char != "") {
            children += `<td><strong>${char}</strong></td>`;
        } else {
            children += `<td><br></td>`;
        }

        // Key

        if (key != "") {
            children += `<td>${key}</td>`;
        } else {
            children += `<td><br></td>`;
        }

        // Liste

        csvChars.push({"key" : key, "char" : char});

        // Fin de tableau

        children += "</tr>";

        children = children.replace(/\\\?/g, "?");

        tabChars.innerHTML += children;
    }
}

// Suppression

function resetText() {
	if (confirm("Tout effacer ?"))	fText.value = null;
}

// Sélection

function selectText(event) {
	event.select();
	event.setSelectionRange(0, 99999);

	document.execCommand("copy");
}

/* Codes */

if (tabChars != null) {
    const code = tabChars.getAttribute("code");

    fetchChars(code);
}