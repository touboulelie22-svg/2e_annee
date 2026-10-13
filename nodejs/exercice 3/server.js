// server.js
const http = require('node:http');

const server = http.createServer((req, res) => {
    // Log de la requête reçue
    console.log(`${req.method} ${req.url}`);

    // En-tête commun à toutes les réponses
    res.setHeader('Content-Type', 'text/plain; charset=utf-8');

    if (req.method === 'GET' && req.url === '/') {
        res.statusCode = 200;
        res.end('Bienvenue sur le serveur Node');
    } else if (req.method === 'GET' && req.url === '/hello') {
        res.statusCode = 200;
        res.end('Hello World');
    } else if (req.method === 'GET' && req.url === '/time') {
        res.statusCode = 200;
        res.end(new Date().toISOString());
    } else {
        res.statusCode = 404;
        res.end('Route inconnue');
    }
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
    console.log(`Serveur démarré sur http://localhost:${PORT}`);
});