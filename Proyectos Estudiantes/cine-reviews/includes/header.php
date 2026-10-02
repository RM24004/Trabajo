<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/auth.php';

$currentUser = currentUser();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $pageTitle ?? APP_NAME ?></title>
    <link rel="stylesheet" href="<?= APP_URL ?>/css/style.css">
</head>
<body>
    <header class="navbar">
        <div class="container nav-container">
            <a href="<?= APP_URL ?>" class="logo">&#127916; CineReviews</a>
            <nav class="nav-links">
                <a href="<?= APP_URL ?>">Inicio</a>
                <a href="<?= APP_URL ?>/pages/movies.php">Peliculas</a>
                <?php if ($currentUser): ?>
                    <a href="<?= APP_URL ?>/pages/add_movie.php">Agregar Pelicula</a>
                    <a href="<?= APP_URL ?>/pages/my_reviews.php">Mis Resenas</a>
                    <span class="nav-user">Hola, <?= sanitize($currentUser['username']) ?></span>
                    <a href="<?= APP_URL ?>/pages/logout.php" class="btn btn-sm btn-outline">Salir</a>
                <?php else: ?>
                    <a href="<?= APP_URL ?>/pages/login.php" class="btn btn-sm btn-outline">Iniciar Sesion</a>
                    <a href="<?= APP_URL ?>/pages/register.php" class="btn btn-sm btn-primary">Registrarse</a>
                <?php endif; ?>
            </nav>
        </div>
    </header>
    <main class="container">
        <?php
        $success = flash('success');
        $error = flash('error');
        if ($success): ?>
            <div class="alert alert-success"><?= $success ?></div>
        <?php endif;
        if ($error): ?>
            <div class="alert alert-error"><?= $error ?></div>
        <?php endif; ?>
