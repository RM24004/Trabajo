<?php
require_once __DIR__ . '/../config/config.php';
$pageTitle = 'Registro - CineReviews';
require_once __DIR__ . '/../includes/header.php';

if (isLoggedIn()) {
    header('Location: ' . APP_URL);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    require_once __DIR__ . '/../models/User.php';
    $user = new User();
    $username = trim($_POST['username'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';
    $confirm = $_POST['confirm_password'] ?? '';

    $errors = [];
    if (strlen($username) < 3) $errors[] = 'El usuario debe tener al menos 3 caracteres';
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Email no valido';
    if (strlen($password) < 6) $errors[] = 'La contrasena debe tener al menos 6 caracteres';
    if ($password !== $confirm) $errors[] = 'Las contrasenas no coinciden';
    if ($user->usernameExists($username)) $errors[] = 'El usuario ya existe';
    if ($user->emailExists($email)) $errors[] = 'El email ya esta registrado';

    if (empty($errors)) {
        $user->register($username, $email, $password);
        flash('success', 'Registro exitoso. Ahora inicia sesion.');
        header('Location: ' . APP_URL . '/pages/login.php');
        exit;
    } else {
        flash('error', implode('<br>', $errors));
    }
}
?>

<div class="auth-container">
    <h1>Crear Cuenta</h1>
    <form method="POST" class="form">
        <div class="form-group">
            <label for="username">Usuario</label>
            <input type="text" id="username" name="username" required minlength="3"
                   value="<?= sanitize($_POST['username'] ?? '') ?>">
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required
                   value="<?= sanitize($_POST['email'] ?? '') ?>">
        </div>
        <div class="form-group">
            <label for="password">Contrasena</label>
            <input type="password" id="password" name="password" required minlength="6">
        </div>
        <div class="form-group">
            <label for="confirm_password">Confirmar Contrasena</label>
            <input type="password" id="confirm_password" name="confirm_password" required>
        </div>
        <button type="submit" class="btn btn-primary btn-block">Registrarse</button>
    </form>
    <p class="auth-link">Ya tienes cuenta? <a href="<?= APP_URL ?>/pages/login.php">Inicia sesion</a></p>
</div>

<?php require_once __DIR__ . '/../includes/footer.php'; ?>
