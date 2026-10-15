const express = require('express');
const path = require('path');

const app = express();

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

app.get('/profil', (req, res) => {
    res.render('profil', {
        prenom: 'caca',
        ville: 'cacaland'
    });
});

app.listen(3000, () => {
    console.log('Serveur démarré sur le port 3000');
});