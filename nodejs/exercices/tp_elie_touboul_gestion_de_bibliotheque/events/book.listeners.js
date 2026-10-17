const bookEmitter = require('./book.events');

bookEmitter.on('book:added', (book) => {
    console.log('Book created:', book.titre);
});

bookEmitter.on('book:deleted', (bookId) => {
    console.log('Book deleted, id:', bookId);
});