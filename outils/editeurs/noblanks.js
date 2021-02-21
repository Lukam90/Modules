/* Variables */

const fText = document.getElementById('text');

/* Conversion */

function convertText() {
	const sText = fText.value;
	const lines = sText.split("\n");

	let res = "";

	for (const line of lines) {
		if (line.trim() != "")	res += `${line}\n`;
	}

	fText.value = res;

	selectText(fText);
}