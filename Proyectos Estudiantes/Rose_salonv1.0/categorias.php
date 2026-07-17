<?php
$pageTitle = 'Categorías';
require_once 'includes/header.php';

$db = getDB();

$categorias = $db->query("SELECT * FROM categorias ORDER BY nombre")->fetchAll();

$slugActual = isset($_GET['slug']) ? $_GET['slug'] : '';
$buscar = isset($_GET['buscar']) ? trim($_GET['buscar']) : '';
$productos = [];

if ($buscar) {
    $pageTitle = 'Resultados: ' . $buscar;
    $term = "%{$buscar}%";
    $stmt = $db->prepare("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE p.activo = 1 AND (p.nombre LIKE ? OR p.descripcion LIKE ? OR c.nombre LIKE ?) ORDER BY p.nombre");
    $stmt->execute([$term, $term, $term]);
    $productos = $stmt->fetchAll();
} elseif ($slugActual) {
    $stmt = $db->prepare("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE c.slug = ? AND p.activo = 1 ORDER BY p.nombre");
    $stmt->execute([$slugActual]);
    $productos = $stmt->fetchAll();
} else {
    $productos = $db->query("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE p.activo = 1 ORDER BY p.nombre")->fetchAll();
}
?>

<section class="page-banner">
    <h1><?= $buscar ? 'Resultados para: "' . htmlspecialchars($buscar) . '"' : 'Nuestras Categorías' ?></h1>
</section>

<section class="categorias-layout">
    <aside class="sidebar-categorias">
        <h3>Categorías</h3>
        <ul>
            <li><a href="categorias.php" class="<?= empty($slugActual) ? 'active' : '' ?>">Todos los productos</a></li>
            <?php foreach ($categorias as $cat): ?>
            <li>
                <a href="categorias.php?slug=<?= htmlspecialchars($cat['slug']) ?>" class="<?= $slugActual === $cat['slug'] ? 'active' : '' ?>">
                    <?= htmlspecialchars($cat['nombre']) ?>
                </a>
            </li>
            <?php endforeach; ?>
        </ul>
    </aside>

    <div class="productos-lista">
        <?php if (empty($productos)): ?>
            <p class="sin-productos">No se encontraron productos en esta categoría.</p>
        <?php else: ?>
            <?php foreach ($productos as $prod): ?>
            <div class="producto-lista-card" data-id="<?= $prod['id'] ?>">
                <img src="<?= htmlspecialchars($prod['imagen']) ?>" alt="<?= htmlspecialchars($prod['nombre']) ?>">
                <div class="producto-lista-info">
                    <span class="producto-categoria"><?= htmlspecialchars($prod['categoria_nombre']) ?></span>
                    <h3><?= htmlspecialchars($prod['nombre']) ?></h3>
                    <p><?= htmlspecialchars($prod['descripcion']) ?></p>
                    <div class="producto-lista-footer">
                        <span class="producto-precio">$<?= number_format($prod['precio'], 2) ?></span>
                        <button class="btn-agregar" data-id="<?= $prod['id'] ?>" data-nombre="<?= htmlspecialchars($prod['nombre']) ?>" data-precio="<?= $prod['precio'] ?>" data-imagen="<?= htmlspecialchars($prod['imagen']) ?>">Agregar al Carrito</button>
                    </div>
                </div>
            </div>
            <?php endforeach; ?>
        <?php endif; ?>
    </div>
</section>

<?php require_once 'includes/footer.php'; ?>
