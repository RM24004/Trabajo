<?php
require_once __DIR__ . '/../config/database.php';
session_start();

$pageTitle = isset($pageTitle) ? $pageTitle . ' | Rose Beauty' : 'Rose Beauty El Salvador';
$currentPage = basename($_SERVER['PHP_SELF'], '.php');
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $pageTitle ?></title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<header>
    <nav>
        <a href="index.php" class="logo-link">
            <img src="assets/img/logo.png" alt="Rose Beauty" class="logo">
        </a>
        <ul>
            <li><a href="index.php" class="<?= $currentPage === 'index' ? 'active' : '' ?>">Inicio</a></li>
            <li><a href="categorias.php" class="<?= $currentPage === 'categorias' ? 'active' : '' ?>">Categorías</a></li>
            <li><a href="nosotros.php" class="<?= $currentPage === 'nosotros' ? 'active' : '' ?>">Nosotros</a></li>
            <li><a href="#" id="btnCarrito">Carrito <span id="carritoContador" class="carrito-contador">0</span></a></li>
        </ul>
        <div class="buscador-container">
            <input type="text" id="buscador" placeholder="Buscar maquillaje...">
        </div>
    </nav>
</header>
<main>
