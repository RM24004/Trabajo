<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Review.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$reviewModel = new Review();
$movieModel = new Movie();
$pageTitle = 'Editar Resena - CineReviews';

$id = $_GET['id'] ?? null;
if (!$id) { header('Location: ' . APP_URL); exit; }

$review = $reviewModel->findById($id);
if (!$review || $review['user_id'] != $_SESSION['user_id']) {
    header('Location: ' . APP_URL);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $rating = (int)($_POST['rating'] ?? 0);
    $title = trim($_POST['title'] ?? '');
    $comment = trim($_POST['comment'] ?? '');

    if ($rating < 1 || $rating > 5 || empty($title) || empty($comment)) {
        flash('error', 'Completa todos los campos correctamente');
    } else {
        $reviewModel->update($id, $rating, $title, $comment);
        $movieModel->updateRating($review['movie_id']);
        flash('success', 'Resena actualizada');
        header('Location: ' . APP_URL . '/pages/movie.php?id=' . $review['movie_id']);
        exit;
    }
}

require_once __DIR__ . '/../includes/header.php';
?>

<h1>Editar Resena: <?= sanitize($review['movie_title']) ?></h1>

<form method="POST" class="form form-wide">
    <div class="form-group">
        <label>Calificacion *</label>
        <div class="star-rating">
            <?php for ($i = 1; $i <= 5; $i++): ?>
                <label class="star-radio">
                    <input type="radio" name="rating" value="<?= $i ?>" required
                        <?= (int)($review['rating'] ?? 0) === $i ? 'checked' : '' ?>>
                    <span class="star">&#9733;</span>
                </label>
            <?php endfor; ?>
        </div>
    </div>

    <div class="form-group">
        <label for="title">Titulo de la resena *</label>
        <input type="text" id="title" name="title" required
               value="<?= sanitize($review['title']) ?>">
    </div>

    <div class="form-group">
        <label for="comment">Tu resena *</label>
        <textarea id="comment" name="comment" rows="6" required><?= sanitize($review['comment']) ?></textarea>
    </div>

    <div class="form-actions">
        <button type="submit" class="btn btn-primary">Guardar Cambios</button>
        <a href="<?= APP_URL ?>/pages/movie.php?id=<?= $review['movie_id'] ?>" class="btn btn-outline">Cancelar</a>
    </div>
</form>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
