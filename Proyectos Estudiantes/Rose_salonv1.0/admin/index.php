<?php
require_once __DIR__ . '/auth.php';
requireLogin();

$db = getDB();

$totalCategorias = $db->query("SELECT COUNT(*) FROM categorias")->fetchColumn();
$totalProductos = $db->query("SELECT COUNT(*) FROM productos")->fetchColumn();
$totalProductosActivos = $db->query("SELECT COUNT(*) FROM productos WHERE activo = 1")->fetchColumn();
$totalCupones = $db->query("SELECT COUNT(*) FROM cupones WHERE activo = 1")->fetchColumn();

$ultimosProductos = $db->query("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id ORDER BY p.created_at DESC LIMIT 5")->fetchAll();

include __DIR__ . '/header_admin.php';
?>

<div class="dashboard">
    <h1>Dashboard</h1>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-icon">📦</div>
            <div class="stat-info">
                <span class="stat-number"><?= $totalProductos ?></span>
                <span class="stat-label">Productos</span>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">📂</div>
            <div class="stat-info">
                <span class="stat-number"><?= $totalCategorias ?></span>
                <span class="stat-label">Categorías</span>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">✅</div>
            <div class="stat-info">
                <span class="stat-number"><?= $totalProductosActivos ?></span>
                <span class="stat-label">Activos</span>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🎟️</div>
            <div class="stat-info">
                <span class="stat-number"><?= $totalCupones ?></span>
                <span class="stat-label">Cupones</span>
            </div>
        </div>
    </div>

    <div class="panel-reciente">
        <h2>Últimos Productos Agregados</h2>
        <table class="tabla">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Categoría</th>
                    <th>Precio</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($ultimosProductos as $prod): ?>
                <tr>
                    <td><?= htmlspecialchars($prod['nombre']) ?></td>
                    <td><?= htmlspecialchars($prod['categoria_nombre']) ?></td>
                    <td>$<?= number_format($prod['precio'], 2) ?></td>
                    <td>
                        <span class="badge <?= $prod['activo'] ? 'badge-success' : 'badge-danger' ?>">
                            <?= $prod['activo'] ? 'Activo' : 'Inactivo' ?>
                        </span>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</div>

<?php include __DIR__ . '/footer_admin.php'; ?>
