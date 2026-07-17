<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$db = getDB();

if (isset($_GET['eliminar'])) {
    $id = (int) $_GET['eliminar'];
    $stmt = $db->prepare("DELETE FROM categorias WHERE id = ?");
    $stmt->execute([$id]);
    header('Location: categorias.php?msg=eliminada');
    exit;
}

$categorias = $db->query("SELECT c.*, (SELECT COUNT(*) FROM productos WHERE categoria_id = c.id) AS total_productos FROM categorias c ORDER BY c.nombre")->fetchAll();

include __DIR__ . '/header_admin.php';
?>

<div class="page-header">
    <h1>Gestionar Categorías</h1>
    <a href="categoria_form.php" class="btn btn-primary">+ Nueva Categoría</a>
</div>

<?php if (isset($_GET['msg'])): ?>
    <div class="alert alert-success">
        <?php
        $msgs = [
            'creada' => 'Categoría creada correctamente',
            'editada' => 'Categoría editada correctamente',
            'eliminada' => 'Categoría eliminada correctamente',
        ];
        echo $msgs[$_GET['msg']] ?? 'Operación completada';
        ?>
    </div>
<?php endif; ?>

<table class="tabla">
    <thead>
        <tr>
            <th>ID</th>
            <th>Imagen</th>
            <th>Nombre</th>
            <th>Slug</th>
            <th>Descripción</th>
            <th>Productos</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        <?php if (empty($categorias)): ?>
        <tr><td colspan="7" class="text-center">No hay categorías</td></tr>
        <?php else: ?>
        <?php foreach ($categorias as $cat): ?>
        <tr>
            <td><?= $cat['id'] ?></td>
            <td>
                <?php if ($cat['imagen']): ?>
                    <img src="../<?= htmlspecialchars($cat['imagen']) ?>" alt="" class="thumb-sm">
                <?php else: ?>
                    <span class="sin-imagen">Sin imagen</span>
                <?php endif; ?>
            </td>
            <td><strong><?= htmlspecialchars($cat['nombre']) ?></strong></td>
            <td><code><?= htmlspecialchars($cat['slug']) ?></code></td>
            <td class="text-truncate"><?= htmlspecialchars($cat['descripcion'] ?? '') ?></td>
            <td><span class="badge badge-info"><?= $cat['total_productos'] ?></span></td>
            <td class="acciones">
                <a href="categoria_form.php?id=<?= $cat['id'] ?>" class="btn btn-sm btn-warning">Editar</a>
                <a href="?eliminar=<?= $cat['id'] ?>" class="btn btn-sm btn-danger" onclick="return confirm('¿Eliminar esta categoría? Los productos asociados también se eliminarán.')">Eliminar</a>
            </td>
        </tr>
        <?php endforeach; ?>
        <?php endif; ?>
    </tbody>
</table>

<?php include __DIR__ . '/footer_admin.php'; ?>
