<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../models/Review.php';
$pageTitle = 'Películas - CineReviews';
require_once __DIR__ . '/../includes/header.php';

$movieModel = new Movie();
$search = trim($_GET['search'] ?? '');
$genre = $_GET['genre'] ?? '';
$order = $_GET['order'] ?? 'newest';

$movies = $movieModel->getAll($search, $genre, $order);
$genres = $movieModel->getGenres();
?>

<h1>Peliculas</h1>

<div class="filters">
    <form method="GET" class="filter-form">
        <input type="text" name="search" placeholder="Buscar pelicula o director..."
               value="<?= sanitize($search) ?>">
        <select name="genre">
            <option value="">Todos los generos</option>
            <?php foreach ($genres as $g): ?>
                <option value="<?= sanitize($g) ?>" <?= $genre === $g ? 'selected' : '' ?>><?= sanitize($g) ?></option>
            <?php endforeach; ?>
        </select>
        <select name="order">
            <option value="newest" <?= $order === 'newest' ? 'selected' : '' ?>>Mas recientes</option>
            <option value="rating" <?= $order === 'rating' ? 'selected' : '' ?>>Mejor calificadas</option>
            <option value="year" <?= $order === 'year' ? 'selected' : '' ?>>Por ano</option>
        </select>
        <button type="submit" class="btn btn-primary">Buscar</button>
    </form>
</div>

<div class="movie-grid">
    <?php if (empty($movies)): ?>
        <p class="no-results">No se encontraron peliculas.</p>
    <?php else: ?>
        <?php foreach ($movies as $movie): ?>
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
                    <span class="genre-tag"><?= sanitize($movie['genre']) ?></span>
                </div>
            </div>
        <?php endforeach; ?>
    <?php endif; ?>
</div>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
