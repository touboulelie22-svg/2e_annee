let livres = [
    { id: 1, titre: 'harry potter', auteur: 'J. K. Rowling', disponible: true },
    { id: 2, titre: 'dragons des tempêtes', auteur: 'Julie Kagawa', disponible: false }
];

let nextId = 3;

const getAllLivres = () => {
    return livres;
};

const getLivreById = (id) => {
    return livres.find((livre) => livre.id === id);
};

const addLivre = (titre, auteur) => {
    const livre = { id: nextId, titre: titre, auteur: auteur, disponible: true };
    nextId++;
    livres.push(livre);
    return livre;
};

const deleteLivre = (id) => {
    const position = livres.findIndex(livre => livre.id === id);
    if (position === -1) {
        return false;
    }
    livres.splice(position, 1);
    return true;
};

const updateLivre = (id, titre, auteur) => {
    const livre = getLivreById(id);
    if (!livre) {
        return undefined;
    }
    livre.titre = titre;
    livre.auteur = auteur;
    return livre;
};

module.exports = {
    getAllLivres,
    getLivreById,
    addLivre,
    deleteLivre,
    updateLivre
};