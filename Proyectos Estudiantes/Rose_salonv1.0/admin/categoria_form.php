<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$db = getDB();
$id = isset($_GET['id']) ? (int) $_GET['id'] : 0;
$categoria = null;
$titulo = 'Nueva Categoría';

if ($id > 0) {
    $stmt = $db->prepare("SELECT * FROM categorias WHERE id = ?");
    $stmt->execute([$id]);
    $categoria = $stmt->fetch();
    if (!$categoria) {
        header('Location: categorias.php');
        exit;
    }
    $titulo = 'Editar Categoría';
}

$error = '';
$exito = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = trim($_POST['nombre'] ?? '');
    $descripcion = trim($_POST['descripcion'] ?? '');
    $slug = trim($_POST['slug'] ?? '');

    if (empty($nombre)) {
        $error = 'El nombre es obligatorio';
    } else {
        if (empty($slug)) {
            $slug = strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $nombre), '-'));
        }

        $imagenPath = $categoria['imagen'] ?? '';

        if (!empty($_FILES['imagen']['name'])) {
            $permitidos = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
            if (in_array($_FILES['imagen']['type'], $permitidos)) {
                $dir = __DIR__ . '/../assets/img/categorias/';
                if (!is_dir($dir)) {
                    mkdir($dir, 0755, true);
                }
                $extension = pathinfo($_FILES['imagen']['name'], PATHINFO_EXTENSION);
                $nombreArchivo = 'cat_' . $slug . '_' . time() . '.' . $extension;
                move_uploaded_file($_FILES['imagen']['tmp_name'], $dir . $nombreArchivo);
                $imagenPath = 'assets/img/categorias/' . $nombreArchivo;
            } else {
                $error = 'Formato de imagen no válido (jpeg, png, gif, webp)';
            }
        }

        if (empty($error)) {
            if ($id > 0) {
                $stmt = $db->prepare("UPDATE categorias SET nombre = ?, descripcion = ?, slug = ?, imagen = ? WHERE id = ?");
                $stmt->execute([$nombre, $descripcion, $slug, $imagenPath, $id]);
                header('Location: categorias.php?msg=editada');
            } else {
                $stmt = $db->prepare("INSERT INTO categorias (nombre, descripcion, slug, imagen) VALUES (?, ?, ?, ?)");
                $stmt->execute([$nombre, $descripcion, $slug, $imagenPath]);
                header('Location: categorias.php?msg=creada');
            }
            exit;
        }
    }
}

include __DIR__ . '/header_admin.php';
?>

<div class="page-header">
    <h1><?= $titulo ?></h1>
    <a href="categorias.php" class="btn btn-secondary">← Volver</a>
</div>

<?php if ($error): ?>
    <div class="alert alert-error"><?= htmlspecialchars($error) ?></div>
<?php endif; ?>

<div class="form-card">
    <form method="POST" enctype="multipart/form-data">
        <div class="form-row">
            <div class="form-group">
                <label for="nombre">Nombre *</label>
                <input type="text" id="nombre" name="nombre" required value="<?= htmlspecialchars($categoria['nombre'] ?? $_POST['nombre'] ?? '') ?>">
            </div>
            <div class="form-group">
                <label for="slug">Slug (auto-generado si se deja vacío)</label>
                <input type="text" id="slug" name="slug" value="<?= htmlspecialchars($categoria['slug'] ?? $_POST['slug'] ?? '') ?>">
            </div>
        </div>
        <div class="form-group">
            <label for="descripcion">Descripción</label>
            <textarea id="descripcion" name="descripcion" rows="3"><?= htmlspecialchars($categoria['descripcion'] ?? $_POST['descripcion'] ?? '') ?></textarea>
        </div>
        <div class="form-group">
            <label for="imagen">Imagen <?= $id > 0 ? '(dejar vacío para mantener la actual)' : '' ?></label>
            <input type="file" id="imagen" name="imagen" accept="image/*">
            <?php if (!empty($categoria['imagen'])): ?>
                <div class="preview-actual">
                    <p>Imagen actual:</p>
                    <img src="../<?= htmlspecialchars($categoria['imagen']) ?>" alt="" class="thumb-md">
                </div>
            <?php endif; ?>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn btn-primary"><?= $id > 0 ? 'Guardar Cambios' : 'Crear Categoría' ?></button>
        </div>
    </form>
</div>

<script>
document.getElementById('nombre').addEventListener('input', function() {
    var slug = this.value
        .toLowerCase()
        .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
    document.getElementById('slug').value = slug;
});
</script>

<?php include __DIR__ . '/footer_admin.php'; ?>
