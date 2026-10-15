const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();

// Notre moteur de templates
app.engine('html', (filePath, options, callback) => {
    fs.readFile(filePath, 'utf8', (err, content) => {
        if (err) {
            return callback(err);
        }

        const htmlFinal = content.replace('{{nom}}', options.nom);

        return callback(null, htmlFinal);
    });
});

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html');

app.get('/', (req, res) => {
    res.render('accueil', {
        nom: 'Alex'
    });
});

app.listen(3000, () => {
    console.log('Serveur démarré sur le port 3000');
});