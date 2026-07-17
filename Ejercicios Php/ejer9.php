<!DOCTYPE html>
<html>
<body>

<form method="POST">

Nota 1:
<input type="number" step="0.01" name="n1"><br><br>

Nota 2:
<input type="number" step="0.01" name="n2"><br><br>

Nota 3:
<input type="number" step="0.01" name="n3"><br><br>

<input type="submit">

</form>
<?php
if(isset($_POST["n1"])){
    $promedio=($_POST["n1"]+$_POST["n2"]+$_POST["n3"])/3;
    echo "Promedio: ".$promedio."<br>";
    if($promedio>=6){
        echo "Aprobado";
    }else{
        echo "Reprobado";
    }
}
?>
</body>
</html>