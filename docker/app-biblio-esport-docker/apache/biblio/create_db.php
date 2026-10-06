<?php
$servername = "mysql";  // Correspond au nom du conteneur MySQL
$username = "root";
$password = "1234";
$dbname = "library";

// Créer la connexion
$conn = new mysqli($servername, $username, $password);

// Vérifier la connexion
if ($conn->connect_error) {
    die("❌ Connection failed: " . $conn->connect_error);
}

// Vérifier si la base de données existe avant de la créer
$sql = "CREATE DATABASE IF NOT EXISTS $dbname";
if ($conn->query($sql) === TRUE) {
    echo "✅ Database created successfully or already exists.<br>";
} else {
    echo "❌ Error creating database: " . $conn->error;
}

// Sélectionner la base de données
$conn->select_db($dbname);

// Vérifier si la table existe avant de la créer
$sql = "CREATE TABLE IF NOT EXISTS books (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL
)";
if ($conn->query($sql) === TRUE) {
    echo "✅ Table 'books' created successfully or already exists.<br>";
} else {
    echo "❌ Error creating table: " . $conn->error;
}

$conn->close();
?>
