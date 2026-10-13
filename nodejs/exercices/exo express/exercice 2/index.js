const express = require("express");

const app = express();

app.get("/bonjour", (req, res) => {
    res.send("Bonjour !");
});

app.get("/a-propos", (req, res) => {
    res.send("Je suis Elie et j'apprends Express.");
});

app.get("/contact", (req, res) => {
    res.send("contact@monsite.fr");
});

app.listen(3000, () => {
    console.log("Serveur démarré sur le port 3000");
});
``