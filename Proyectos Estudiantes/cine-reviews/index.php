<?php
require_once __DIR__ . '/config/config.php';
require_once __DIR__ . '/models/Movie.php';
require_once __DIR__ . '/models/Review.php';

$movieModel = new Movie();
$reviewModel = new Review();

$topMovies = $movieModel->getTopRated(5);
$recentReviews = $reviewModel->getRecent(5);
$totalMovies = $movieModel->countAll();
$totalReviews = $reviewModel->countAll();

$pageTitle = 'CineReviews - Plataforma de Resenas de Peliculas';
require_once __DIR__ . '/includes/header.php';
?>

<section class="hero">
    <h1>Bienvenido a CineReviews</h1>
    <p>Descubre, califica y comparte tus peliculas favoritas</p>
    <div class="hero-stats">
        <div class="stat">
            <span class="stat-num"><?= $totalMovies ?></span>
            <span class="stat-label">Peliculas</span>
        </div>
        <div class="stat">
            <span class="stat-num"><?= $totalReviews ?></span>
            <span class="stat-label">Resenas</span>
        </div>
    </div>
    <div class="hero-actions">
        <a href="<?= APP_URL ?>/pages/movies.php" class="btn btn-primary">Explorar Peliculas</a>
        <?php if (!isLoggedIn()): ?>
            <a href="<?= APP_URL ?>/pages/register.php" class="btn btn-outline">Crear Cuenta</a>
        <?php else: ?>
            <a href="<?= APP_URL ?>/pages/add_movie.php" class="btn btn-outline">Agregar Pelicula</a>
        <?php endif; ?>
    </div>
</section>

<section class="home-section">
    <h2>Mejor Calificadas</h2>
    <div class="movie-grid">
        <?php foreach ($topMovies as $movie): ?>
            <div class="movie-card">
                <a href="<?= APP_URL ?>/pages/movie.php?id=<?= $movie['id'] ?>">
                    <img src="<?= sanitize($movie['poster_url'] ?: 'https://via.placeholder.com/300x450?text=' . urlencode($movie['title'])) ?>"
                         alt="<?= sanitize($movie['title']) ?>">
                </a>
                <div class="movie-card-info">
                    <h3><a href="<?= APP_URL ?>/pages/movie.php?id=<?= $movie['id'] ?>"><?= sanitize($movie['title']) ?></a></h3>
                    <div class="rating">
                        <span class="stars"><?= str_repeat('&#9733;', round($movie['rating_avg'])) ?><?= str_repeat('&#9734;', 5 - round($movie['rating_avg'])) ?></span>
                        <span class="rating-num"><?= number_format($movie['rating_avg'], 1) ?></span>
                    </div>
                    <p class="meta"><?= sanitize($movie['director']) ?> &middot; <?= $movie['release_year'] ?></p>
                </div>
            </div>
        <?php endforeach; ?>
    </div>
</section>

<section class="home-section">
    <h2>Resenas Recientes</h2>
    <div class="reviews-list">
        <?php foreach ($recentReviews as $review): ?>
            <div class="review-card">
                <div class="review-header">
                    <span class="review-user"><?= sanitize($review['username']) ?></span>
                    <span class="review-rating"><?= str_repeat('&#9733;', $review['rating']) ?><?= str_repeat('&#9734;', 5 - $review['rating']) ?></span>
                    <span class="review-date"><?= date('d/m/Y', strtotime($review['created_at'])) ?></span>
                </div>
                <h3><?= sanitize($review['movie_title']) ?></h3>
                <h4><?= sanitize($review['title']) ?></h4>
                <p><?= nl2br(sanitize($review['comment'])) ?></p>
                <a href="<?= APP_URL ?>/pages/movie.php?id=<?= $review['movie_id'] ?>" class="btn btn-sm btn-primary">Ver pelicula</a>
            </div>
        <?php endforeach; ?>
    </div>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
