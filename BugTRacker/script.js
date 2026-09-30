// ===== Données =====
const bugs = [];

let prochainId = 1;
const prioritesValides = ["low", "high"];

function generatebugs(liste, title, description, priority){
    if (title.trim() === "") {
        return null;
    }
    if (!prioritesValides.includes(priority)) {
        return null;
    }

    const bug = {
        id: prochainId,
        title: title.trim(),
        description: description,
        priority: priority,
        status: "open",
        createdAt: new Date().toISOString().slice(0, 10)
    };

    prochainId++;
    liste.push(bug);
    return bug;
}

// ===== Tests =====
const listeTest = [];
console.assert(ajouterBug(listeTest, "", "d", "low") === null, "Titre vide refusé");
console.assert(ajouterBug(listeTest, "   ", "d", "low") === null, "Titre d'espaces refusé");
console.assert(ajouterBug(listeTest, "Bug A", "d", "high") !== null, "Bug valide accepté");
console.assert(listeTest.length === 1, "Un seul bug dans la liste");
console.assert(listeTest[0].status === "open", "Statut initial open");
console.assert(ajouterBug(listeTest, "Bug B", "d", "banane") === null, "Priorité invalide refusée");
console.assert(ajouterBug(listeTest, "Bug C", "d", "low") !== null, "Priorité low acceptée");
prochainId = 1;


function changerStatut(liste, id) {
    const bug = liste.find(function (b) {
        return b.id === id;
    });

    if (bug === undefined) {
        return false;
    }

    bug.status = bug.status === "open" ? "closed" : "open";
    return true;
}