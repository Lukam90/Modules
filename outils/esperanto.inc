@header

:Des <a href="/cookies.html" target="_blank">cookies</a> sont utilisés sur ce site afin d'améliorer l'expérience utilisateur.

<hr>

:<a href="#chars-list" onclick="toggleLink();">Tableau de conversion</a>

<div id="chars-list" style="display: none;">
:Les caractères remplacés sont les suivants :

<table id="chars" code="EO"></table>
</div>

<hr>

<h2>Texte</h2>

:<textarea class="big-text" id="lines" rows="10" cols="50"></textarea>

:<button class="big-btn" onclick="convertText('EO');">Convertir</button>

<hr>

<h2>Résultat</h2>

:<textarea class="big-text" id="result" rows="10" cols="50" onclick="this.select();" readonly></textarea>

<hr>

<h2>Sauvegarde</h2>

<p>
    Nom du fichier : <input type="text" id="filename">
    <select id="extension">
        <option value="txt" selected>Texte (.txt)</option>
        <option value="md">Markdown (.md)</option>
    </select>
</p>

:Le texte sera automatiquement converti lors de la sauvegarde.

:<button class="big-btn" onclick="saveText();">Enregistrer</button>

<script src="./editeurs/keyboard.js"></script>

@end