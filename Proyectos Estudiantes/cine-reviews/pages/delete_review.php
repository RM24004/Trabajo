<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Review.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$reviewModel = new Review();
$movieModel = new Movie();

$id = $_GET['id'] ?? null;
$movieId = $_GET['movie_id'] ?? null;

if ($id) {
    $review = $reviewModel->findById($id);
    if ($review && $review['user_id'] == $_SESSION['user_id']) {
        $reviewModel->delete($id);
        $movieModel->updateRating($review['movie_id']);
        flash('success', 'Resena eliminada');
    }
}

header('Location: ' . APP_URL . '/pages/movie.php?id=' . ($movieId ?? ($review['movie_id'] ?? '')));
exit;
