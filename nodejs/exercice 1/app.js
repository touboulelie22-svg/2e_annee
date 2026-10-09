const fs = require('fs');
const path = require('path');
const filePath = path.json(__dirname,"data", "user.json")

fs.readFile(filePath, "utf8", (err, data) => {
    // Gestion des erreurs de lecture
    if (err) {
        console.error("Erreur lors de la lecture du fichier :", err.message);
        return;
    }

    try {
        // Conversion du JSON en objet JavaScript
        const users = JSON.parse(data);

        // Affichage des noms des utilisateurs
        console.log("Liste des utilisateurs :");
        users.forEach(user => {
            console.log(user.name);
        });
    } catch (parseError) {
        // Gestion des erreurs de JSON invalide
        console.error("Erreur : le fichier contient un JSON invalide.");
        console.error(parseError.message);
    }
});