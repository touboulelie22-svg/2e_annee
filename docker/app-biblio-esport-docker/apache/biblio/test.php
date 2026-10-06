<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "mysql";
$username = "root";
$password = "1234";
$dbname = "library";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("❌ Connection failed: " . $conn->connect_error);
}

echo "✅ Connected to MySQL successfully!<br>";

$sql = "SELECT id, title, author, genre FROM books";
$result = $conn->query($sql);

if (!$result) {
    die("❌ SQL Error: " . $conn->error);
} else {
    echo "✅ Query executed successfully!<br>";
}

phpinfo();