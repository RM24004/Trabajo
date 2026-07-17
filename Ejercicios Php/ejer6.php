<!DOCTYPE html>
<html>
<body>

<form method="POST">

Número:
<input type="number" name="numero">

<input type="submit">

</form>

<?php

if(isset($_POST["numero"])){

    $numero = $_POST["numero"];

    echo "<h2>Tabla del $numero</h2>";

    for($i=1; $i<=10; $i++){

        echo "$numero x $i = ".($numero*$i)."<br>";

    }
}
?>
</body>
</html>