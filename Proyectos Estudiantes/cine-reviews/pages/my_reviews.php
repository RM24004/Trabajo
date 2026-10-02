<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Review.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$reviewModel = new Review();
$pageTitle = 'Mis Resenas - CineReviews';

$reviews = $reviewModel->getByUser($_SESSION['user_id']);

require_once __DIR__ . '/../includes/header.php';
?>

<h1>Mis Resenas</h1>

<?php if (empty($reviews)): ?>
    <p class="no-results">No has escrito ninguna resena aun.</p>
    <a href="<?= APP_URL ?>/pages/movies.php" class="btn btn-primary">Explorar peliculas</a>
<?php else: ?>
    <div class="reviews-list">
        <?php foreach ($reviews as $review): ?>
            <div class="review-card">
                <div class="review-header">
                    <span class="review-rating"><?= str_repeat('&#9733;', $review['rating']) ?><?= str_repeat('&#9734;', 5 - $review['rating']) ?></span>
                    <span class="review-date"><?= date('d/m/Y', strtotime($review['created_at'])) ?></span>
                </div>
                <h3><?= sanitize($review['movie_title']) ?></h3>
                <h4><?= sanitize($review['title']) ?></h4>
                <p><?= nl2br(sanitize($review['comment'])) ?></p>
                <div class="review-actions">
                    <a href="<?= APP_URL ?>/pages/movie.php?id=<?= $review['movie_id'] ?>" class="btn btn-sm btn-primary">Ver pelicula</a>
                    <a href="<?= APP_URL ?>/pages/edit_review.php?id=<?= $review['id'] ?>" class="btn btn-sm btn-secondary">Editar</a>
                    <a href="<?= APP_URL ?>/pages/delete_review.php?id=<?= $review['id'] ?>&movie_id=<?= $review['movie_id'] ?>"
                       class="btn btn-sm btn-danger"
                       onclick="return confirm('Eliminar esta resena?')">Eliminar</a>
                </div>
            </div>
        <?php endforeach; ?>
    </div>
<?php endif; ?>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
