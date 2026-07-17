<?php
header('Content-Type: application/json');
require_once __DIR__ . '/../config/database.php';

$codigo = isset($_GET['codigo']) ? trim(strtoupper($_GET['codigo'])) : '';

if (empty($codigo)) {
    echo json_encode(['exito' => false, 'mensaje' => 'Código de cupón requerido']);
    exit;
}

try {
    $db = getDB();
    $stmt = $db->prepare("SELECT * FROM cupones WHERE codigo = ? AND activo = 1 AND (fecha_expiracion IS NULL OR fecha_expiracion >= CURDATE())");
    $stmt->execute([$codigo]);
    $cupon = $stmt->fetch();

    if ($cupon) {
        echo json_encode([
            'exito' => true,
            'codigo' => $cupon['codigo'],
            'descuento' => $cupon['descuento'],
            'tipo' => $cupon['tipo'],
            'min_compra' => $cupon['min_compra']
        ]);
    } else {
        echo json_encode(['exito' => false, 'mensaje' => 'Cupón inválido o expirado']);
    }
} catch (Exception $e) {
    echo json_encode(['exito' => false, 'mensaje' => 'Error del servidor']);
}
