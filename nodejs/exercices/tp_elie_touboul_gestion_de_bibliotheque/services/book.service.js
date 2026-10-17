let books = [
    { id: 1, titre: 'harry potter', auteur: 'J. K. Rowling', disponible: true },
    { id: 2, titre: 'dragons des tempêtes', auteur: 'Julie Kagawa', disponible: false }
];

let nextId = 3;

const getAllBooks = () => {
    return books;
};

const getBookById = (id) => {
    return books.find((book) => book.id === id);
};

const addBook = (titre, auteur) => {
    const book = { id: nextId, titre: titre, auteur: auteur, disponible: true };
    nextId++;
    books.push(book);
    return book;
};

const deleteBook = (id) => {
    const position = books.findIndex(book => book.id === id);
    if (position === -1) {
        return false;
    }
    books.splice(position, 1);
    return true;
};

const updateBook = (id, titre, auteur) => {
    const book = getBookById(id);
    if (!book) {
        return undefined;
    }
    book.titre = titre;
    book.auteur = auteur;
    return book;
};

module.exports = {
    getAllBooks,
    getBookById,
    addBook,
    deleteBook,
    updateBook
};