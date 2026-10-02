<?php
require_once __DIR__ . '/../config/config.php';
$pageTitle = 'Login - CineReviews';
require_once __DIR__ . '/../includes/header.php';

if (isLoggedIn()) {
    header('Location: ' . APP_URL);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_once __DIR__ . '/../models/User.php';
    $user = new User();
    $email = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';

    $found = $user->login($email, $password);
    if ($found) {
        $_SESSION['user_id'] = $found['id'];
        header('Location: ' . APP_URL);
        exit;
    } else {
        flash('error', 'Email o contrasena incorrectos');
    }
}
?>

<div class="auth-container">
    <h1>Iniciar Sesion</h1>
    <form method="POST" class="form">
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Contrasena</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit" class="btn btn-primary btn-block">Ingresar</button>
    </form>
    <p class="auth-link">No tienes cuenta? <a href="<?= APP_URL ?>/pages/register.php">Registrate</a></p>
    <p class="auth-hint">Usuarios de prueba: admin@cinereviews.com / password</p>
</div>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
