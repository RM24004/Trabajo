<?php

$mostrar = false;
$color = "black";
$promedio = 0;
$estado = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $carnet = $_POST["carnet"];
    $nombre = $_POST["nombre"];
    $apellido = $_POST["apellido"];
    $edad = $_POST["edad"];
    $sexo = $_POST["sexo"];
    $carrera = $_POST["carrera"];
    $ciclo = $_POST["ciclo"];

    $nota1 = $_POST["nota1"];
    $nota2 = $_POST["nota2"];
    $nota3 = $_POST["nota3"];

    $comentario = $_POST["comentario"];

    $materias = isset($_POST["materias"]) ? $_POST["materias"] : [];

    $promedio = ($nota1 + $nota2 + $nota3) / 3;

    if ($promedio >= 6) {
        $estado = "APROBADO";
        $color = "green";
    } else {
        $estado = "REPROBADO";
        $color = "red";
    }

    $mostrar = true;
}

?>

<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<title>Registro de Estudiantes</title>

<style>

body{

    font-family:Arial;
    background: #5982c0;
    margin:0;
    padding:30px;

}

.contenedor{

    width:700px;
    margin:auto;
    background: #c9c9c9;
    padding:30px;
    border-radius:10px;
    box-shadow:0px 0px 10px gray;

}

h1{

    text-align:center;
    color:#2c3e50;

}

input[type=text],
input[type=number],
select,
textarea{

    width:100%;
    padding:10px;
    border:1px solid #37a0c0;
    border-radius:6px;
    box-sizing:border-box;
    margin-top:5px;
    margin-bottom:15px;

}

input[type=radio],
input[type=checkbox]{

    width:auto;
    margin-right:8px;

}

button{

background:#0d6efd;

color:white;
font-size:18px;
padding:15px;
border:none;
border-radius:8px;
cursor:pointer;
transition:.3s;

}

button:hover{

background:#084298;
transform:scale(1.02);

}

.tarjeta{

    margin-top:40px;
    border:2px solid #34495e;
    border-radius:10px;
    padding:25px;
    background:#f8f9fa;

}

.estado{

    font-size:22px;
    font-weight:bold;

}
.form-grid{

    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;

}
.notas{

display:grid;
grid-template-columns:repeat(3,1fr);
gap:15px;

}

.checkbox-group label{

display:block;
margin:8px 0;

}

</style>

</head>

<body>

<div class="contenedor">

<h1>Registro de Estudiantes</h1>

<form method="POST">

<label>Carnet</label>
<input type="text" name="carnet" required>

<label>Nombre</label>
<input type="text" name="nombre" required>

<label>Apellido</label>
<input type="text" name="apellido" required>

<label>Edad</label>
<input type="number" name="edad" required>

<label>Sexo</label>

<input type="radio" name="sexo" value="Masculino" required> Masculino
<input type="radio" name="sexo" value="Femenino"> Femenino

<br><br>

<label>Carrera</label>

<select name="carrera">

<option>Ingeniería en Sistemas</option>
<option>Administración</option>
<option>Contabilidad</option>
<option>Diseño Gráfico</option>

</select>

<label>Ciclo</label>

<select name="ciclo">

<option>I</option>
<option>II</option>
<option>III</option>
<option>IV</option>
<option>V</option>

</select>

<label>Nota 1</label>
<input type="number" step="0.01" name="nota1" required>

<label>Nota 2</label>
<input type="number" step="0.01" name="nota2" required>

<label>Nota 3</label>
<input type="number" step="0.01" name="nota3" required>

<label>Materias Favoritas</label>

<input type="checkbox" name="materias[]" value="Programación"> Programación<br>

<input type="checkbox" name="materias[]" value="Base de Datos"> Base de Datos<br>

<input type="checkbox" name="materias[]" value="Redes"> Redes<br>

<input type="checkbox" name="materias[]" value="Matemática"> Matemática<br>

<input type="checkbox" name="materias[]" value="Diseño Web"> Diseño Web<br><br>

<label>Comentarios</label>

<textarea name="comentario" rows="5"></textarea>

<button type="submit">Registrar Estudiante</button>

</form>

<?php

if($mostrar){

?>

<div class="tarjeta">

<h2 align="center">FICHA DEL ESTUDIANTE</h2>

<hr>

<p><strong>Carnet:</strong> <?php echo $carnet; ?></p>

<p><strong>Nombre:</strong> <?php echo $nombre." ".$apellido; ?></p>

<p><strong>Edad:</strong> <?php echo $edad; ?> años</p>

<p><strong>Sexo:</strong> <?php echo $sexo; ?></p>

<p><strong>Carrera:</strong> <?php echo $carrera; ?></p>

<p><strong>Ciclo:</strong> <?php echo $ciclo; ?></p>

<p><strong>Materias Favoritas:</strong></p>

<ul>

<?php

foreach($materias as $materia){

    echo "<li>$materia</li>";

}

?>

</ul>

<p><strong>Nota 1:</strong> <?php echo $nota1; ?></p>

<p><strong>Nota 2:</strong> <?php echo $nota2; ?></p>

<p><strong>Nota 3:</strong> <?php echo $nota3; ?></p>

<p><strong>Promedio:</strong> <?php echo number_format($promedio,2); ?></p>

<p class="estado" style="color:<?php echo $color; ?>;">

<?php echo $estado; ?>

</p>

<p><strong>Comentarios:</strong></p>

<p><?php echo $comentario; ?></p>

</div>

<?php

}

?>

</div>

</body>

</html>