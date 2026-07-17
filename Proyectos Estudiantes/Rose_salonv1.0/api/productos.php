<?php
header('Content-Type: application/json');
require_once __DIR__ . '/../config/database.php';

$search = isset($_GET['q']) ? trim($_GET['q']) : '';

if (empty($search)) {
    echo json_encode([]);
    exit;
}

try {
    $db = getDB();
    $stmt = $db->prepare("SELECT p.*, c.nombre AS categoria_nombre FROM productos p JOIN categorias c ON p.categoria_id = c.id WHERE p.activo = 1 AND (p.nombre LIKE ? OR p.descripcion LIKE ? OR c.nombre LIKE ?) ORDER BY p.nombre LIMIT 20");
    $term = "%{$search}%";
    $stmt->execute([$term, $term, $term]);
    $productos = $stmt->fetchAll();
    echo json_encode($productos);
} catch (Exception $e) {
    echo json_encode([]);
}
