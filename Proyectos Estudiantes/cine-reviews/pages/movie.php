<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../models/Review.php';
require_once __DIR__ . '/../includes/auth.php';

$movieModel = new Movie();
$reviewModel = new Review();

$id = $_GET['id'] ?? null;
if (!$id) { header('Location: ' . APP_URL . '/pages/movies.php'); exit; }

$movie = $movieModel->findById($id);
if (!$movie) { header('Location: ' . APP_URL . '/pages/movies.php'); exit; }

$pageTitle = $movie['title'] . ' - CineReviews';
$reviews = $reviewModel->getByMovie($id);
$hasReviewed = isLoggedIn() ? $reviewModel->hasUserReviewed($_SESSION['user_id'], $id) : false;

require_once __DIR__ . '/../includes/header.php';
?>

<div class="movie-detail">
    <div class="movie-detail-poster">
        <img src="<?= sanitize($movie['poster_url'] ?: 'https://via.placeholder.com/300x450?text=' . urlencode($movie['title'])) ?>"
             alt="<?= sanitize($movie['title']) ?>">
    </div>
    <div class="movie-detail-info">
        <h1><?= sanitize($movie['title']) ?></h1>
        <div class="rating-large">
            <span class="stars"><?= str_repeat('&#9733;', round($movie['rating_avg'])) ?><?= str_repeat('&#9734;', 5 - round($movie['rating_avg'])) ?></span>
            <span class="rating-num"><?= number_format($movie['rating_avg'], 1) ?> / 5</span>
        </div>
        <p class="meta"><?= sanitize($movie['director']) ?> &middot; <?= $movie['release_year'] ?> &middot; <?= sanitize($movie['genre']) ?></p>
        <p class="synopsis"><?= nl2br(sanitize($movie['synopsis'])) ?></p>

        <div class="movie-actions">
            <?php if (isLoggedIn()): ?>
                <?php if (!$hasReviewed): ?>
                    <a href="<?= APP_URL ?>/pages/add_review.php?movie_id=<?= $movie['id'] ?>" class="btn btn-primary">Escribir Resena</a>
                <?php else: ?>
                    <span class="btn btn-disabled">Ya has reseñado esta pelicula</span>
                <?php endif; ?>
            <?php else: ?>
                <a href="<?= APP_URL ?>/pages/login.php" class="btn btn-outline">Inicia sesion para reseñar</a>
            <?php endif; ?>
            <?php if (isLoggedIn()): ?>
                <a href="<?= APP_URL ?>/pages/edit_movie.php?id=<?= $movie['id'] ?>" class="btn btn-secondary">Editar</a>
                <a href="<?= APP_URL ?>/pages/delete_movie.php?id=<?= $movie['id'] ?>" class="btn btn-danger"
                   onclick="return confirm('Seguro que deseas eliminar esta pelicula?')">Eliminar</a>
            <?php endif; ?>
        </div>
    </div>
</div>

<section class="reviews-section">
    <h2>Resenas (<?= count($reviews) ?>)</h2>
    <?php if (empty($reviews)): ?>
        <p class="no-results">No hay resenas todavia.</p>
    <?php else: ?>
        <?php foreach ($reviews as $review): ?>
            <div class="review-card">
                <div class="review-header">
                    <span class="review-user"><?= sanitize($review['username']) ?></span>
                    <span class="review-rating"><?= str_repeat('&#9733;', $review['rating']) ?><?= str_repeat('&#9734;', 5 - $review['rating']) ?></span>
                    <span class="review-date"><?= date('d/m/Y', strtotime($review['created_at'])) ?></span>
                </div>
                <h3><?= sanitize($review['title']) ?></h3>
                <p><?= nl2br(sanitize($review['comment'])) ?></p>
                <?php if (isLoggedIn() && $_SESSION['user_id'] === $review['user_id']): ?>
                    <div class="review-actions">
                        <a href="<?= APP_URL ?>/pages/edit_review.php?id=<?= $review['id'] ?>" class="btn btn-sm btn-secondary">Editar</a>
                        <a href="<?= APP_URL ?>/pages/delete_review.php?id=<?= $review['id'] ?>&movie_id=<?= $movie['id'] ?>"
                           class="btn btn-sm btn-danger"
                           onclick="return confirm('Eliminar esta resena?')">Eliminar</a>
                    </div>
                <?php endif; ?>
            </div>
        <?php endforeach; ?>
    <?php endif; ?>
</section>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
