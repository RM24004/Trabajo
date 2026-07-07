<?php

$resultado="";

if(isset($_POST["operacion"])){

    $n1=$_POST["n1"];
    $n2=$_POST["n2"];
    $op=$_POST["operacion"];

    switch($op){

        case "+":
            $resultado=$n1+$n2;
        break;

        case "-":
            $resultado=$n1-$n2;
        break;

        case "*":
            $resultado=$n1*$n2;
        break;

        case "/":

            if($n2!=0){

                $resultado=$n1/$n2;

            }else{

                $resultado="No se puede dividir entre cero";

            }

        break;

        case "^":

            $resultado=pow($n1,$n2);

        break;

        case "raiz":

            $resultado=sqrt($n1);

        break;

    }

}

?>

<!DOCTYPE html>
<html>

<head>

<title>Calculadora PHP</title>

<style>

body{

background:#2c3e50;
font-family:Arial;
display:flex;
justify-content:center;
align-items:center;
height:100vh;

}

.calculadora{

background:white;
padding:30px;
border-radius:15px;
width:350px;
box-shadow:0 0 15px black;

}

input{

width:100%;
padding:12px;
margin:8px 0;
font-size:18px;

}

.botones{

display:grid;
grid-template-columns:repeat(3,1fr);
gap:10px;

}

button{

padding:15px;
font-size:18px;
background:#3498db;
color:white;
border:none;
cursor:pointer;
border-radius:8px;

}

button:hover{

background:#2980b9;

}

.resultado{

margin-top:20px;
background:#ecf0f1;
padding:15px;
font-size:22px;
text-align:center;

}

</style>

</head>

<body>

<div class="calculadora">

<h2 align="center">Calculadora PHP</h2>

<form method="POST">

<input type="number" step="any" name="n1" placeholder="Primer número">

<input type="number" step="any" name="n2" placeholder="Segundo número">

<div class="botones">

<button name="operacion" value="+">+</button>

<button name="operacion" value="-">-</button>

<button name="operacion" value="*">*</button>

<button name="operacion" value="/">/</button>

<button name="operacion" value="^">x²</button>

<button name="operacion" value="raiz">√</button>

</div>

</form>

<div class="resultado">

<?php echo $resultado; ?>

</div>

</div>

</body>

</html>