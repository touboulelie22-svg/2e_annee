<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "mysql";  // Doit correspondre au nom du conteneur MySQL
$username = "root";
$password = "1234";
$dbname = "library";

// Connexion à MySQL
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("❌ Connection failed: " . $conn->connect_error);
}

// Vérifier si la table 'books' existe
$table_exists = $conn->query("SHOW TABLES LIKE 'books'");

if ($table_exists->num_rows == 0) {
    // Création de la table 'books' si elle n'existe pas
    $sql_create = "CREATE TABLE books (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        genre VARCHAR(50) NOT NULL
    )";
    
    if ($conn->query($sql_create) === TRUE) {
        echo "✅ Table 'books' créée avec succès.<br>";
    } else {
        die("❌ Erreur lors de la création de la table: " . $conn->error);
    }

    // Insérer 50 livres
    $sql_insert = "INSERT INTO books (title, author, genre) VALUES
        ('1984', 'George Orwell', 'Dystopian'),
        ('To Kill a Mockingbird', 'Harper Lee', 'Fiction'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic'),
        ('Moby Dick', 'Herman Melville', 'Adventure'),
        ('Pride and Prejudice', 'Jane Austen', 'Romance'),
        ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction'),
        ('Brave New World', 'Aldous Huxley', 'Dystopian'),
        ('War and Peace', 'Leo Tolstoy', 'Historical'),
        ('Crime and Punishment', 'Fyodor Dostoevsky', 'Psychological Fiction'),
        ('The Odyssey', 'Homer', 'Epic'),
        ('Jane Eyre', 'Charlotte Bronte', 'Romance'),
        ('Wuthering Heights', 'Emily Bronte', 'Gothic'),
        ('Fahrenheit 451', 'Ray Bradbury', 'Dystopian'),
        ('Frankenstein', 'Mary Shelley', 'Horror'),
        ('Dracula', 'Bram Stoker', 'Horror'),
        ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy'),
        ('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy'),
        ('The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy'),
        ('Alice in Wonderland', 'Lewis Carroll', 'Fantasy'),
        ('The Little Prince', 'Antoine de Saint-Exupery', 'Children'),
        ('Les Misérables', 'Victor Hugo', 'Historical'),
        ('The Divine Comedy', 'Dante Alighieri', 'Epic'),
        ('Anna Karenina', 'Leo Tolstoy', 'Romance'),
        ('Madame Bovary', 'Gustave Flaubert', 'Realism'),
        ('Don Quixote', 'Miguel de Cervantes', 'Adventure'),
        ('The Metamorphosis', 'Franz Kafka', 'Surrealism'),
        ('The Picture of Dorian Gray', 'Oscar Wilde', 'Gothic'),
        ('A Tale of Two Cities', 'Charles Dickens', 'Historical'),
        ('Great Expectations', 'Charles Dickens', 'Classic'),
        ('Oliver Twist', 'Charles Dickens', 'Classic'),
        ('David Copperfield', 'Charles Dickens', 'Classic'),
        ('The Count of Monte Cristo', 'Alexandre Dumas', 'Adventure'),
        ('The Three Musketeers', 'Alexandre Dumas', 'Adventure'),
        ('The Stranger', 'Albert Camus', 'Existentialism'),
        ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Magical Realism'),
        ('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical'),
        ('The Idiot', 'Fyodor Dostoevsky', 'Psychological Fiction'),
        ('The Trial', 'Franz Kafka', 'Surrealism'),
        ('Catch-22', 'Joseph Heller', 'Satire'),
        ('Slaughterhouse-Five', 'Kurt Vonnegut', 'Satire'),
        ('The Bell Jar', 'Sylvia Plath', 'Autobiographical Fiction'),
        ('Beloved', 'Toni Morrison', 'Historical'),
        ('Invisible Man', 'Ralph Ellison', 'Social Commentary'),
        ('Ulysses', 'James Joyce', 'Modernist'),
        ('Mrs. Dalloway', 'Virginia Woolf', 'Modernist'),
        ('Orlando', 'Virginia Woolf', 'Fantasy'),
        ('To the Lighthouse', 'Virginia Woolf', 'Modernist'),
        ('The Sound and the Fury', 'William Faulkner', 'Stream of Consciousness'),
        ('As I Lay Dying', 'William Faulkner', 'Southern Gothic')
    ";

    if ($conn->query($sql_insert) === TRUE) {
        echo "✅ 50 livres insérés avec succès.<br>";
    } else {
        die("❌ Erreur lors de l’insertion des données: " . $conn->error);
    }
}

// Récupérer la liste des livres
$sql_select = "SELECT id, title, author, genre FROM books";
$result = $conn->query($sql_select);

?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Livres</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .row {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }
        .book-card {
            width: 18%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #f9f9f9;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>📚 Liste des Livres dans la Bibliothèque</h1>
    <div id="books">
        <?php
        $count = 0; // Compteur de livres affichés

        if ($result->num_rows > 0) {
            echo "<div class='row'>"; // Ouvre la première ligne
            
            while ($row = $result->fetch_assoc()) {
                echo "<div class='book-card'>";
                echo "<h3>" . htmlspecialchars($row["title"]) . "</h3>";
                echo "<p>Auteur: " . htmlspecialchars($row["author"]) . "</p>";
                echo "<p>Genre: " . htmlspecialchars($row["genre"]) . "</p>";
                echo "</div>";

                $count++;

                // Tous les 5 livres, on ferme la ligne et on en ouvre une nouvelle (sauf pour le dernier groupe)
                if ($count % 5 == 0 && $count < 50) {
                    echo "</div><div class='row'>";
                }
            }
            
            echo "</div>"; // Ferme la dernière ligne
        } else {
            echo "<p>Aucun livre trouvé.</p>";
        }
        ?>
    </div>
</body>
</html>


<?php $conn->close(); ?>
