<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$db = getDB();

if (isset($_GET['eliminar'])) {
    $id = (int) $_GET['eliminar'];
    $stmt = $db->prepare("DELETE FROM productos WHERE id = ?");
    $stmt->execute([$id]);
    header('Location: productos.php?msg=eliminado');
    exit;
}

$categoriaFiltro = isset($_GET['categoria']) ? (int) $_GET['categoria'] : 0;

if ($categoriaFiltro > 0) {
    $stmt = $db->prepare("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE p.categoria_id = ? ORDER BY p.nombre");
    $stmt->execute([$categoriaFiltro]);
    $productos = $stmt->fetchAll();
} else {
    $productos = $db->query("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id ORDER BY p.nombre")->fetchAll();
}

$categorias = $db->query("SELECT * FROM categorias ORDER BY nombre")->fetchAll();

include __DIR__ . '/header_admin.php';
?>

<div class="page-header">
    <h1>Gestionar Productos</h1>
    <div class="page-header-actions">
        <select id="filtroCategoria" onchange="window.location='productos.php?categoria='+this.value">
            <option value="0">Todas las categorías</option>
            <?php foreach ($categorias as $cat): ?>
            <option value="<?= $cat['id'] ?>" <?= $categoriaFiltro == $cat['id'] ? 'selected' : '' ?>><?= htmlspecialchars($cat['nombre']) ?></option>
            <?php endforeach; ?>
        </select>
        <a href="producto_form.php" class="btn btn-primary">+ Nuevo Producto</a>
    </div>
</div>

<?php if (isset($_GET['msg'])): ?>
    <div class="alert alert-success">
        <?php
        $msgs = [
            'creado' => 'Producto creado correctamente',
            'editado' => 'Producto editado correctamente',
            'eliminado' => 'Producto eliminado correctamente',
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
            <th>Categoría</th>
            <th>Precio</th>
            <th>Stock</th>
            <th>Tendencia</th>
            <th>Estado</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        <?php if (empty($productos)): ?>
        <tr><td colspan="9" class="text-center">No hay productos</td></tr>
        <?php else: ?>
        <?php foreach ($productos as $prod): ?>
        <tr>
            <td><?= $prod['id'] ?></td>
            <td>
                <?php if ($prod['imagen']): ?>
                    <img src="../<?= htmlspecialchars($prod['imagen']) ?>" alt="" class="thumb-sm">
                <?php else: ?>
                    <span class="sin-imagen">Sin imagen</span>
                <?php endif; ?>
            </td>
            <td><strong><?= htmlspecialchars($prod['nombre']) ?></strong></td>
            <td><span class="badge badge-info"><?= htmlspecialchars($prod['categoria_nombre']) ?></span></td>
            <td>$<?= number_format($prod['precio'], 2) ?></td>
            <td>
                <span class="<?= $prod['stock'] < 10 ? 'text-danger' : '' ?>"><?= $prod['stock'] ?></span>
            </td>
            <td>
                <?= $prod['tendencia'] ? '<span class="badge badge-warning">⭐ Sí</span>' : 'No' ?>
            </td>
            <td>
                <span class="badge <?= $prod['activo'] ? 'badge-success' : 'badge-danger' ?>">
                    <?= $prod['activo'] ? 'Activo' : 'Inactivo' ?>
                </span>
            </td>
            <td class="acciones">
                <a href="producto_form.php?id=<?= $prod['id'] ?>" class="btn btn-sm btn-warning">Editar</a>
                <a href="?eliminar=<?= $prod['id'] ?>" class="btn btn-sm btn-danger" onclick="return confirm('¿Eliminar este producto?')">Eliminar</a>
            </td>
        </tr>
        <?php endforeach; ?>
        <?php endif; ?>
    </tbody>
</table>

<?php include __DIR__ . '/footer_admin.php'; ?>
