const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const server = http.createServer((req, res) => {
    const filePath = path.join(__dirname, 'template.html');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            res.writeHead(500, {
                'Content-Type': 'text/plain; charset=utf-8'
            });

            return res.end('Erreur 500 : impossible de lire le template');
        }

        let html = data;
        html = html.replace('{{prenom}}', 'Camille');
        html = html.replace('{{ville}}', 'Lyon');

        res.writeHead(200, {
            'Content-Type': 'text/html; charset=utf-8'
        });

        res.end(html);
    });
});

server.listen(3000, () => {
    console.log('Serveur démarré sur http://localhost:3000');
});