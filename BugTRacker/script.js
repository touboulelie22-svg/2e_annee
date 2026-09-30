// ===== Données =====
const bugs = [];
let prochainId = 1;
const prioritesValides = ["low", "high"];

// ===== Fonctions métier =====

function ajouterBug(liste, title, description, priority) {
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

function supprimerBug(liste, id) {
    const index = liste.findIndex(function (b) {
        return b.id === id;
    });

    if (index === -1) {
        return false;
    }

    liste.splice(index, 1);
    return true;
}

function filtrerParPriorite(liste, priority) {
    if (priority === "all") {
        return liste;
    }

    return liste.filter(function (b) {
        return b.priority === priority;
    });
}

function rechercherParTitre(liste, texte) {
    const recherche = texte.trim().toLowerCase();

    return liste.filter(function (b) {
        return b.title.toLowerCase().includes(recherche);
    });
}

function compterBugs(liste) {
    let open = 0;
    let closed = 0;

    for (const bug of liste) {
        if (bug.status === "open") {
            open++;
        } else {
            closed++;
        }
    }

    return { open: open, closed: closed };
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

const idTest = listeTest[0].id;
console.assert(changerStatut(listeTest, idTest) === true, "Changement réussi");
console.assert(listeTest[0].status === "closed", "open devient closed");
changerStatut(listeTest, idTest);
console.assert(listeTest[0].status === "open", "closed redevient open");
console.assert(changerStatut(listeTest, 9999) === false, "Id inconnu");

console.assert(supprimerBug(listeTest, idTest) === true, "Suppression réussie");
console.assert(listeTest.length === 1, "Il reste un bug");
console.assert(listeTest[0].title === "Bug C", "Le bon bug est resté");
console.assert(supprimerBug(listeTest, 9999) === false, "Suppression d'un id inconnu");

const listeFiltre = [];
ajouterBug(listeFiltre, "Bug X", "d", "high");
ajouterBug(listeFiltre, "Bug Y", "d", "low");
ajouterBug(listeFiltre, "Bug Z", "d", "high");
console.assert(filtrerParPriorite(listeFiltre, "high").length === 2, "Deux bugs high");
console.assert(filtrerParPriorite(listeFiltre, "low").length === 1, "Un bug low");
console.assert(filtrerParPriorite(listeFiltre, "all").length === 3, "all renvoie tout");
console.assert(filtrerParPriorite([], "high").length === 0, "Liste vide");

const listeRecherche = [];
ajouterBug(listeRecherche, "Erreur formulaire", "d", "high");
ajouterBug(listeRecherche, "Bouton cassé", "d", "low");
console.assert(rechercherParTitre(listeRecherche, "formulaire").length === 1, "Recherche simple");
console.assert(rechercherParTitre(listeRecherche, "FORMULAIRE").length === 1, "Insensible à la casse");
console.assert(rechercherParTitre(listeRecherche, "").length === 2, "Recherche vide renvoie tout");
console.assert(rechercherParTitre(listeRecherche, "zzz").length === 0, "Aucun résultat");

const listeCompte = [];
console.assert(compterBugs(listeCompte).open === 0, "Liste vide : 0 ouvert");
ajouterBug(listeCompte, "Bug 1", "d", "high");
ajouterBug(listeCompte, "Bug 2", "d", "low");
changerStatut(listeCompte, listeCompte[0].id);
console.assert(compterBugs(listeCompte).open === 1, "Un bug ouvert");
console.assert(compterBugs(listeCompte).closed === 1, "Un bug fermé");

prochainId = 1;