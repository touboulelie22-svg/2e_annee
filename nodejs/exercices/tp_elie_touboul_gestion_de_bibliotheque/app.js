const bookRoutes = require('./routes/book.routes');
const express = require('express');
const morgan = require('morgan')
require('./events/book.listeners');
const app = express();

app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use('/books', bookRoutes);
app.listen(3000, () => {
    console.log('Server is running on port 3000!');
});