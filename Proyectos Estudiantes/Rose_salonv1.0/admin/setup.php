<?php
require_once __DIR__ . '/../config/database.php';

$mensaje = '';
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuario = trim($_POST['usuario'] ?? '');
    $password = $_POST['password'] ?? '';
    $nombre = trim($_POST['nombre'] ?? '');

    if (empty($usuario) || empty($password) || empty($nombre)) {
        $error = 'Todos los campos son obligatorios';
    } elseif (strlen($password) < 6) {
        $error = 'La contraseña debe tener al menos 6 caracteres';
    } else {
        try {
            $db = getDB();

            // Crear tabla admins si no existe
            $db->exec("CREATE TABLE IF NOT EXISTS admins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB");

            $hash = password_hash($password, PASSWORD_DEFAULT);
            $stmt = $db->prepare("INSERT INTO admins (usuario, password, nombre) VALUES (?, ?, ?)");
            $stmt->execute([$usuario, $hash, $nombre]);

            $mensaje = "Usuario '$usuario' creado correctamente. Ya puedes ir a <a href='login.php'>Iniciar Sesión</a>";
        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $error = "El usuario '$usuario' ya existe";
            } else {
                $error = "Error: " . $e->getMessage();
            }
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Setup Admin - Rose Beauty</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #d1b8c6, #bb97aa); min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.15); width: 100%; max-width: 450px; }
        h1 { color: #6b3d57; text-align: center; margin-bottom: 5px; }
        h2 { color: #999; text-align: center; font-weight: 400; margin-bottom: 25px; font-size: 1rem; }
        .form-group { margin-bottom: 18px; }
        label { display: block; margin-bottom: 6px; font-weight: 600; color: #555; font-size: 0.9rem; }
        input { width: 100%; padding: 12px 16px; border: 2px solid #e0e0e0; border-radius: 10px; font-size: 0.95rem; outline: none; }
        input:focus { border-color: #bb97aa; }
        button { width: 100%; padding: 14px; background: linear-gradient(135deg, #6b3d57, #4a2a3d); color: white; border: none; border-radius: 10px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s; }
        button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(107,61,87,0.3); }
        .alert { padding: 12px 16px; border-radius: 10px; margin-bottom: 20px; font-size: 0.9rem; }
        .alert-success { background: #e8f5e9; color: #2e7d32; }
        .alert-error { background: #fce4ec; color: #c62828; }
        .alert a { font-weight: 700; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Rose Beauty</h1>
        <h2>Crear Usuario Administrador</h2>

        <?php if ($mensaje): ?>
            <div class="alert alert-success"><?= $mensaje ?></div>
        <?php endif; ?>
        <?php if ($error): ?>
            <div class="alert alert-error"><?= htmlspecialchars($error) ?></div>
        <?php endif; ?>

        <form method="POST">
            <div class="form-group">
                <label for="nombre">Nombre completo</label>
                <input type="text" id="nombre" name="nombre" required value="<?= htmlspecialchars($_POST['nombre'] ?? '') ?>">
            </div>
            <div class="form-group">
                <label for="usuario">Usuario (para iniciar sesión)</label>
                <input type="text" id="usuario" name="usuario" required value="<?= htmlspecialchars($_POST['usuario'] ?? '') ?>">
            </div>
            <div class="form-group">
                <label for="password">Contraseña (mínimo 6 caracteres)</label>
                <input type="password" id="password" name="password" required minlength="6">
            </div>
            <button type="submit">Crear Administrador</button>
        </form>
    </div>
</body>
</html>
