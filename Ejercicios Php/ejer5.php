<!DOCTYPE html>
<html>
<body>

<form method="POST">

Número 1:
<input type="number" name="n1"><br><br>

Número 2:
<input type="number" name="n2"><br><br>

<input type="submit">

</form>

<?php

if(isset($_POST["n1"]) && isset($_POST["n2"])){

    $a = $_POST["n1"];
    $b = $_POST["n2"];

    if($a > $b){

        echo "$a es mayor.";

    }elseif($b > $a){

        echo "$b es mayor.";

    }else{

        echo "Los números son iguales.";

    }

}

?>

</body>
</html>