const { getAllBooks, getBookById, addBook, deleteBook, updateBook } = require('../services/book.service');

const listBooks = (req, res) => {
    const books = getAllBooks();
    res.json(books);
};

const showBook = (req, res) => {
    const id = Number(req.params.id);
    const book = getBookById(id);

    if (!book) {
        return res.status(404).json({ message: 'Book not found' });
    }
    res.json(book);
};

const createBook = (req, res) => {
    const { titre, auteur } = req.body;
    if (!titre || !auteur) {
        return res.status(400).json({ message: 'Titre and auteur are required' });
    }
    const book = addBook(titre, auteur);
    res.status(201).json(book);
};

