docker network create esports-network
docker run -d --name mysql --network esports-network -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=library -p 3306:3306 mysql
docker run -d --name mongo --network esports-network -e MONGO_INITDB_ROOT_USERNAME=esportroot -e MONGO_INITDB_ROOT_PASSWORD=password1234 -p 27017:27017 mongo


# Dans le dossier nodejs

docker build -t esports-api .
docker run -d --name esports-api --network esports-network -p 3000:3000 esports-api

# Dans le dossier apache
docker build -t php-apache-app .
docker run -d --name apache-app --network esports-network -p 12345:80 php-apache-app


# Ajout de PHPMYADMIN

docker run -d --name phpmyadmin --network esports-network -e PMA_HOST=mysql -e PMA_USER=root -e PMA_PASSWORD=1234 -p 12346:80 phpmyadmin/phpmyadmin
