<!DOCTYPE html>
<html>
<body>

<form method="POST">

Nombre:
<input type="text" name="nombre"><br><br>

Edad:
<input type="number" name="edad"><br><br>

Carrera:
<input type="text" name="carrera"><br><br>

Promedio:
<input type="number" step="0.01" name="promedio"><br><br>

<input type="submit">

</form>

<?php

if(isset($_POST["nombre"])){

    $nombre=$_POST["nombre"];
    $edad=$_POST["edad"];
    $carrera=$_POST["carrera"];
    $promedio=$_POST["promedio"];

    echo "<hr>";

    echo "<h2>DATOS DEL ESTUDIANTE</h2>";

    echo "Nombre: $nombre <br>";
    echo "Edad: $edad años<br>";
    echo "Carrera: $carrera <br>";
    echo "Promedio: $promedio <br>";

    if($promedio>=6){

        echo "<h3 style='color:green;'>Estado: Aprobado</h3>";

    }else{

        echo "<h3 style='color:red;'>Estado: Reprobado</h3>";

    }

}

?>

</body>
</html>