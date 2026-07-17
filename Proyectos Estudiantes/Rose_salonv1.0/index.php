<?php
$pageTitle = 'Inicio';
require_once 'includes/header.php';

$db = getDB();

$categorias = $db->query("SELECT * FROM categorias ORDER BY nombre")->fetchAll();

$productosTendencia = $db->query("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE p.tendencia = 1 AND p.activo = 1 ORDER BY p.created_at DESC")->fetchAll();
?>

<section class="banner">
    <img src="assets/img/portada.jpg" alt="Rose Beauty - Tienda de cosméticos">
</section>

<section class="seccion-categorias">
    <h1 class="seccion-titulo">Categorías de Productos</h1>
    <div class="grid-categorias">
        <?php foreach ($categorias as $cat): ?>
        <a href="categorias.php?slug=<?= htmlspecialchars($cat['slug']) ?>" class="categoria-card">
            <img src="<?= htmlspecialchars($cat['imagen']) ?>" alt="<?= htmlspecialchars($cat['nombre']) ?>">
            <span><?= htmlspecialchars($cat['nombre']) ?></span>
        </a>
        <?php endforeach; ?>
    </div>
</section>

<section class="seccion-productos">
    <h1 class="seccion-titulo">Productos en Tendencia</h1>
    <div class="grid-productos">
        <?php foreach ($productosTendencia as $prod): ?>
        <div class="producto-card" data-id="<?= $prod['id'] ?>">
            <img src="<?= htmlspecialchars($prod['imagen']) ?>" alt="<?= htmlspecialchars($prod['nombre']) ?>">
            <div class="producto-info">
                <span class="producto-categoria"><?= htmlspecialchars($prod['categoria_nombre']) ?></span>
                <h3><?= htmlspecialchars($prod['nombre']) ?></h3>
                <p class="producto-precio">$<?= number_format($prod['precio'], 2) ?></p>
                <button class="btn-agregar" data-id="<?= $prod['id'] ?>" data-nombre="<?= htmlspecialchars($prod['nombre']) ?>" data-precio="<?= $prod['precio'] ?>" data-imagen="<?= htmlspecialchars($prod['imagen']) ?>">Agregar al Carrito</button>
            </div>
        </div>
        <?php endforeach; ?>
    </div>
</section>

<?php require_once 'includes/footer.php'; ?>
