const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Configuration de Pug
app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

// Route principale
app.get('/', (req, res) => {
    res.render('index');
});

app.listen(PORT, () => {
    console.log(`Serveur démarré sur http://localhost:${PORT}`);
});