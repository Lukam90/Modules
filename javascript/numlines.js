/* Variables */

const fText = document.getElementById('text');

/* Conversion */

function convertText() {
	const sText = fText.value;
	const lines = sText.split("\n");

	let res = "";

	let num = 1;

	for (const line of lines) {
		if (line != "") {
			res += `${num}) ${line}\n`;
			num++;
		}
	}

	fText.value = res;

	selectText(fText);
}