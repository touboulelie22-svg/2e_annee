const express = require('express');
const path = require('path');
const app = express();
 app.set('view engine', 'pug');
 app.set('views', path.join(__dirname, 'views'));

 app.get('/visiteur', (req, res) => {
     res.render('accueil', {
         connecte: true,
         prenom: 'elie'
     });
 });
 app.get('/visiteur', (req, res) => {
     res.render('accueil', {
            connecte: false
     });
 });
 app.listen(3000, () => {
     console.log('serveur démarré sur le port 3000');
 });