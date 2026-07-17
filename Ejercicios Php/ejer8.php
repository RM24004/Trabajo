<!DOCTYPE html>
<html>
<body>
<form method="POST">
Número 1:
<input type="number" name="n1"><br><br>
Número 2:
<input type="number" name="n2"><br><br>
<select name="operacion">
<option value="+">Sumar</option>
<option value="-">Restar</option>
<option value="*">Multiplicar</option>
<option value="/">Dividir</option>
</select>
<br><br>
<input type="submit">
</form>
<?php
if(isset($_POST["n1"])){
    $a=$_POST["n1"];
    $b=$_POST["n2"];
    $op=$_POST["operacion"];
    switch($op){
        case "+":
            echo "Resultado: ".($a+$b);
        break;

        case "-":
            echo "Resultado: ".($a-$b);
        break;

        case "*":
            echo "Resultado: ".($a*$b);
        break;

        case "/":
            echo "Resultado: ".($a/$b);
        break;
    }
}
?>
</body>
</html>