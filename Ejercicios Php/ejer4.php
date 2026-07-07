<!DOCTYPE html>
<html>
<body>

<form method="POST">

Edad:
<input type="number" name="edad">

<input type="submit">

</form>

<?php

if(isset($_POST["edad"])){

    $edad = $_POST["edad"];

    if($edad >= 18){

        echo "Es mayor de edad";

    }else{

        echo "Es menor de edad";

    }

}

?>

</body>
</html>