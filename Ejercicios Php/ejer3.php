<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
</head>
<body>

<form method="POST">
    Nombre:
    <input type="text" name="nombre">
    <input type="submit" value="Enviar">
</form>

<?php

if(isset($_POST["nombre"])){

    $nombre = $_POST["nombre"];

    echo "<h2>Hola $nombre, bienvenido a PHP.</h2>";

}

?>

</body>
</html>