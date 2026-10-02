<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../models/Review.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$movieModel = new Movie();
$reviewModel = new Review();
$pageTitle = 'Escribir Resena - CineReviews';

$movieId = $_GET['movie_id'] ?? $_POST['movie_id'] ?? null;
if (!$movieId) { header('Location: ' . APP_URL . '/pages/movies.php'); exit; }

$movie = $movieModel->findById($movieId);
if (!$movie) { header('Location: ' . APP_URL . '/pages/movies.php'); exit; }

if ($reviewModel->hasUserReviewed($_SESSION['user_id'], $movieId)) {
    flash('error', 'Ya has escrito una resena para esta pelicula');
    header('Location: ' . APP_URL . '/pages/movie.php?id=' . $movieId);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $rating = (int)($_POST['rating'] ?? 0);
    $title = trim($_POST['title'] ?? '');
    $comment = trim($_POST['comment'] ?? '');

    if ($rating < 1 || $rating > 5 || empty($title) || empty($comment)) {
        flash('error', 'Completa todos los campos y selecciona una calificacion');
    } else {
        $reviewModel->create($_SESSION['user_id'], $movieId, $rating, $title, $comment);
        $movieModel->updateRating($movieId);
        flash('success', 'Resena publicada correctamente');
        header('Location: ' . APP_URL . '/pages/movie.php?id=' . $movieId);
        exit;
    }
}

require_once __DIR__ . '/../includes/header.php';
?>

<h1>Resena: <?= sanitize($movie['title']) ?></h1>

<form method="POST" class="form form-wide">
    <input type="hidden" name="movie_id" value="<?= $movieId ?>">

    <div class="form-group">
        <label>Calificacion *</label>
        <div class="star-rating">
            <?php for ($i = 1; $i <= 5; $i++): ?>
                <label class="star-radio">
                    <input type="radio" name="rating" value="<?= $i ?>" required
                        <?= (int)($_POST['rating'] ?? 0) === $i ? 'checked' : '' ?>>
                    <span class="star">&#9733;</span>
                </label>
            <?php endfor; ?>
        </div>
    </div>

    <div class="form-group">
        <label for="title">Titulo de la resena *</label>
        <input type="text" id="title" name="title" required
               value="<?= sanitize($_POST['title'] ?? '') ?>">
    </div>

    <div class="form-group">
        <label for="comment">Tu resena *</label>
        <textarea id="comment" name="comment" rows="6" required><?= sanitize($_POST['comment'] ?? '') ?></textarea>
    </div>

    <div class="form-actions">
        <button type="submit" class="btn btn-primary">Publicar Resena</button>
        <a href="<?= APP_URL ?>/pages/movie.php?id=<?= $movieId ?>" class="btn btn-outline">Cancelar</a>
    </div>
</form>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
