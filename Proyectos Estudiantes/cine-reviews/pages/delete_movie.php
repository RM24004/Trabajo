<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$movieModel = new Movie();
$id = $_GET['id'] ?? null;

if ($id) {
    $movieModel->delete($id);
    flash('success', 'Pelicula eliminada');
}

header('Location: ' . APP_URL . '/pages/movies.php');
exit;
