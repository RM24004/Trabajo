<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../models/Movie.php';
require_once __DIR__ . '/../includes/auth.php';

requireLogin();
$movieModel = new Movie();
$pageTitle = 'Agregar Pelicula - CineReviews';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = [
        'title' => trim($_POST['title'] ?? ''),
        'synopsis' => trim($_POST['synopsis'] ?? ''),
        'director' => trim($_POST['director'] ?? ''),
        'release_year' => (int)($_POST['release_year'] ?? 2024),
        'genre' => trim($_POST['genre'] ?? ''),
        'poster_url' => trim($_POST['poster_url'] ?? ''),
    ];

    if (empty($data['title']) || empty($data['synopsis']) || empty($data['director']) || empty($data['genre'])) {
        flash('error', 'Todos los campos obligatorios deben ser completados');
    } else {
        $movieModel->create($data);
        flash('success', 'Pelicula agregada correctamente');
        header('Location: ' . APP_URL . '/pages/movies.php');
        exit;
    }
}

require_once __DIR__ . '/../includes/header.php';
?>

<h1>Agregar Pelicula</h1>

<form method="POST" class="form form-wide">
    <div class="form-row">
        <div class="form-group">
            <label for="title">Titulo *</label>
            <input type="text" id="title" name="title" required
                   value="<?= sanitize($_POST['title'] ?? '') ?>">
        </div>
        <div class="form-group">
            <label for="director">Director *</label>
            <input type="text" id="director" name="director" required
                   value="<?= sanitize($_POST['director'] ?? '') ?>">
        </div>
    </div>
    <div class="form-row">
        <div class="form-group">
            <label for="release_year">Ano de estreno *</label>
            <input type="number" id="release_year" name="release_year" required min="1900" max="<?= date('Y') + 1 ?>"
                   value="<?= (int)($_POST['release_year'] ?? date('Y')) ?>">
        </div>
        <div class="form-group">
            <label for="genre">Genero *</label>
            <input type="text" id="genre" name="genre" required placeholder="Ej: Drama, Accion, Comedia"
                   value="<?= sanitize($_POST['genre'] ?? '') ?>">
        </div>
    </div>
    <div class="form-group">
        <label for="synopsis">Sinopsis *</label>
        <textarea id="synopsis" name="synopsis" rows="4" required><?= sanitize($_POST['synopsis'] ?? '') ?></textarea>
    </div>
    <div class="form-group">
        <label for="poster_url">URL del poster (opcional)</label>
        <input type="url" id="poster_url" name="poster_url"
               value="<?= sanitize($_POST['poster_url'] ?? '') ?>">
    </div>
    <div class="form-actions">
        <button type="submit" class="btn btn-primary">Agregar Pelicula</button>
        <a href="<?= APP_URL ?>/pages/movies.php" class="btn btn-outline">Cancelar</a>
    </div>
</form>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
