<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$currentPage = basename($_SERVER['PHP_SELF'], '.php');
$adminNombre = $_SESSION['admin_nombre'] ?? 'Admin';
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Rose Beauty</title>
    <link rel="stylesheet" href="../assets/css/admin.css">
</head>
<body>
    <div class="admin-layout">
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>Rose Beauty</h2>
                <span class="admin-badge">Admin</span>
            </div>
            <nav class="sidebar-nav">
                <a href="index.php" class=" <?= $currentPage === 'index' ? 'active' : '' ?>">📊 Dashboard</a>
                <a href="categorias.php" class=" <?= $currentPage === 'categorias' || $currentPage === 'categoria_form' ? 'active' : '' ?>">📂 Categorías</a>
                <a href="productos.php" class=" <?= $currentPage === 'productos' || $currentPage === 'producto_form' ? 'active' : '' ?>">📦 Productos</a>
            </nav>
            <div class="sidebar-footer">
                <span><?= htmlspecialchars($adminNombre) ?></span>
                <a href="logout.php" class="btn-logout">Cerrar Sesión</a>
                <a href="../index.php" class="btn-ver-tienda" target="_blank">Ver Tienda</a>
            </div>
        </aside>
        <main class="admin-main">
