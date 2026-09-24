<?php


$dossier = __DIR__ . '/uploads/';


// Upload

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fichier'])) {


    $nom = basename($_FILES['fichier']['name']);


    $destination = $dossier . $nom;


    if (move_uploaded_file($_FILES['fichier']['tmp_name'], $destination)) {

        $message = "Fichier envoyé avec succès !";

    } else {

        $message = "Erreur lors de l'envoi du fichier.";

    }

}


// Lecture du dossier

$fichiers = array_diff(scandir($dossier), ['.', '..']);


?>


<!DOCTYPE html>


<html lang="fr">


<head>

    <meta charset="UTF-8">

    <title>Upload de fichiers</title>

</head>


<body>


    <h1>Upload de fichiers</h1>


    <form method="POST" enctype="multipart/form-data">


        <input type="file" name="fichier" required>


        <button type="submit">

            Envoyer

        </button>


    </form>


    <?php if (isset($message)): ?>


        <p>

            <?= htmlspecialchars($message) ?>

        </p>


    <?php endif; ?>




    <h2>Liste des fichiers</h2>


    <ul>


        <?php foreach ($fichiers as $fichier): ?>


            <li>

                <?= htmlspecialchars($fichier) ?>

            </li>


        <?php endforeach; ?>


    </ul>


</body>


</html>