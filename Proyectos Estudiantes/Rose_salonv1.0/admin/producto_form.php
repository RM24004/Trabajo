<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$db = getDB();
$id = isset($_GET['id']) ? (int) $_GET['id'] : 0;
$producto = null;
$titulo = 'Nuevo Producto';

if ($id > 0) {
    $stmt = $db->prepare("SELECT * FROM productos WHERE id = ?");
    $stmt->execute([$id]);
    $producto = $stmt->fetch();
    if (!$producto) {
        header('Location: productos.php');
        exit;
    }
    $titulo = 'Editar Producto';
}

$categorias = $db->query("SELECT * FROM categorias ORDER BY nombre")->fetchAll();

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = trim($_POST['nombre'] ?? '');
    $descripcion = trim($_POST['descripcion'] ?? '');
    $precio = floatval($_POST['precio'] ?? 0);
    $categoria_id = (int) ($_POST['categoria_id'] ?? 0);
    $stock = (int) ($_POST['stock'] ?? 0);
    $tendencia = isset($_POST['tendencia']) ? 1 : 0;
    $activo = isset($_POST['activo']) ? 1 : 0;

    if (empty($nombre) || $precio <= 0 || $categoria_id <= 0) {
        $error = 'Nombre, precio y categoría son obligatorios';
    } else {
        $imagenPath = $producto['imagen'] ?? '';

        if (!empty($_FILES['imagen']['name'])) {
            $permitidos = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
            if (in_array($_FILES['imagen']['type'], $permitidos)) {
                $dir = __DIR__ . '/../assets/img/productos/';
                if (!is_dir($dir)) {
                    mkdir($dir, 0755, true);
                }
                $slug = strtolower(preg_replace('/[^A-Za-z0-9]+/', '-', $nombre));
                $extension = pathinfo($_FILES['imagen']['name'], PATHINFO_EXTENSION);
                $nombreArchivo = $slug . '_' . time() . '.' . $extension;
                move_uploaded_file($_FILES['imagen']['tmp_name'], $dir . $nombreArchivo);
                $imagenPath = 'assets/img/productos/' . $nombreArchivo;
            } else {
                $error = 'Formato de imagen no válido';
            }
        }

        if (empty($error)) {
            if ($id > 0) {
                $stmt = $db->prepare("UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, imagen = ?, categoria_id = ?, stock = ?, tendencia = ?, activo = ? WHERE id = ?");
                $stmt->execute([$nombre, $descripcion, $precio, $imagenPath, $categoria_id, $stock, $tendencia, $activo, $id]);
                header('Location: productos.php?msg=editado');
            } else {
                $stmt = $db->prepare("INSERT INTO productos (nombre, descripcion, precio, imagen, categoria_id, stock, tendencia, activo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
                $stmt->execute([$nombre, $descripcion, $precio, $imagenPath, $categoria_id, $stock, $tendencia, $activo]);
                header('Location: productos.php?msg=creado');
            }
            exit;
        }
    }
}

include __DIR__ . '/header_admin.php';
?>

<div class="page-header">
    <h1><?= $titulo ?></h1>
    <a href="productos.php" class="btn btn-secondary">← Volver</a>
</div>

<?php if ($error): ?>
    <div class="alert alert-error"><?= htmlspecialchars($error) ?></div>
<?php endif; ?>

<div class="form-card">
    <form method="POST" enctype="multipart/form-data">
        <div class="form-row">
            <div class="form-group flex-2">
                <label for="nombre">Nombre del producto *</label>
                <input type="text" id="nombre" name="nombre" required value="<?= htmlspecialchars($producto['nombre'] ?? $_POST['nombre'] ?? '') ?>">
            </div>
            <div class="form-group flex-1">
                <label for="precio">Precio ($) *</label>
                <input type="number" id="precio" name="precio" step="0.01" min="0.01" required value="<?= $producto['precio'] ?? $_POST['precio'] ?? '' ?>">
            </div>
        </div>

        <div class="form-group">
            <label for="descripcion">Descripción</label>
            <textarea id="descripcion" name="descripcion" rows="3"><?= htmlspecialchars($producto['descripcion'] ?? $_POST['descripcion'] ?? '') ?></textarea>
        </div>

        <div class="form-row">
            <div class="form-group flex-2">
                <label for="categoria_id">Categoría *</label>
                <select id="categoria_id" name="categoria_id" required>
                    <option value="">Seleccionar categoría</option>
                    <?php foreach ($categorias as $cat): ?>
                    <option value="<?= $cat['id'] ?>" <?= (($producto['categoria_id'] ?? $_POST['categoria_id'] ?? '') == $cat['id']) ? 'selected' : '' ?>>
                        <?= htmlspecialchars($cat['nombre']) ?>
                    </option>
                    <?php endforeach; ?>
                </select>
            </div>
            <div class="form-group flex-1">
                <label for="stock">Stock</label>
                <input type="number" id="stock" name="stock" min="0" value="<?= $producto['stock'] ?? $_POST['stock'] ?? 0 ?>">
            </div>
        </div>

        <div class="form-group">
            <label for="imagen">Imagen <?= $id > 0 ? '(dejar vacío para mantener la actual)' : '' ?></label>
            <input type="file" id="imagen" name="imagen" accept="image/*">
            <?php if (!empty($producto['imagen'])): ?>
                <div class="preview-actual">
                    <p>Imagen actual:</p>
                    <img src="../<?= htmlspecialchars($producto['imagen']) ?>" alt="" class="thumb-md">
                </div>
            <?php endif; ?>
        </div>

        <div class="form-row form-checks">
            <label class="checkbox-label">
                <input type="checkbox" name="tendencia" value="1" <?= ($producto['tendencia'] ?? $_POST['tendencia'] ?? 0) ? 'checked' : '' ?>>
                Producto en tendencia
            </label>
            <label class="checkbox-label">
                <input type="checkbox" name="activo" value="1" <?= ($producto['activo'] ?? $_POST['activo'] ?? 1) ? 'checked' : '' ?>>
                Activo en la tienda
            </label>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn btn-primary"><?= $id > 0 ? 'Guardar Cambios' : 'Crear Producto' ?></button>
        </div>
    </form>
</div>

<?php include __DIR__ . '/footer_admin.php'; ?>
