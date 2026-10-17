const express = require('express');
const router = express.Router();
const { listBooks, showBook, createBook, updateBookById, removeBook } = require('../controllers/book.controller');

router.get('/', listBooks);
router.get('/:id', showBook);
router.post('/', createBook);
router.put('/:id', updateBookById);
router.delete('/:id', removeBook);
module.exports = router;
