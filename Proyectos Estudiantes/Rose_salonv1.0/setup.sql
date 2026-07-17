CREATE DATABASE IF NOT EXISTS rose_beauty CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE rose_beauty;

CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    imagen VARCHAR(255),
    slug VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    imagen VARCHAR(255),
    categoria_id INT NOT NULL,
    stock INT DEFAULT 0,
    tendencia TINYINT(1) DEFAULT 0,
    activo TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS cupones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL UNIQUE,
    descuento DECIMAL(5,2) NOT NULL,
    tipo ENUM('porcentaje', 'fijo') DEFAULT 'porcentaje',
    min_compra DECIMAL(10,2) DEFAULT 0,
    fecha_expiracion DATE,
    activo TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Para crear el usuario admin, ejecuta admin/setup.php después de importar esta base de datos

INSERT INTO categorias (nombre, descripcion, imagen, slug) VALUES
('Labiales', 'Labiales de larga duración y colores vibrantes', 'img/labiales.jpg', 'labiales'),
('Base y Corrector', 'Bases de maquillaje y correctores para todo tipo de piel', 'img/base.jpg', 'base-corrector'),
('Sombras', 'Paletas de sombras y sombras individuales', 'img/sombras.jpg', 'sombras'),
('Rímel y Pestañas', 'Máscaras de pestañas y extensiones', 'img/rimel.jpg', 'rimel-pestanas'),
('Rubores', 'Rubores en polvo, crema y líquido', 'img/rubor.jpg', 'rubores'),
('Iluminador y Contornos', 'Iluminadores y productos de contouring', 'img/iluminador.jpg', 'iluminador-contornos'),
('Cuidado de Piel', 'Skincare: limpiadores, serums y moisturizers', 'img/skincare.jpg', 'cuidado-de-piel'),
('Herramientas', 'Brochas, esponjas y accesorios de maquillaje', 'img/herramientas.jpg', 'herramientas'),
('Fragancias', 'Perfumes y fragancias para ella', 'img/fragancias.jpg', 'fragancias');

INSERT INTO productos (nombre, descripcion, precio, imagen, categoria_id, stock, tendencia) VALUES
('Labial Velvet Rose', 'Labial mate de larga duración con acabado aterciopelado', 12.99, 'img/labial1.jpg', 1, 50, 1),
('Labial Gloss Pink', 'Brillo labial con efecto glossy y color rosa suave', 9.99, 'img/labial2.jpg', 1, 35, 0),
('Labial Liquid Berry', 'Labial líquido matte en tono frambuesa', 11.50, 'img/labial3.jpg', 1, 40, 1),
('Base HD Perfect', 'Base de maquillaje cobertura alta definición', 18.99, 'img/base1.jpg', 2, 30, 1),
('Corrector Instant', 'Corrector de ojeras de cobertura total', 14.50, 'img/corrector1.jpg', 2, 45, 0),
('Paleta Sunset Eyes', '12 sombras con tonos cálidos de atardecer', 24.99, 'img/sombras1.jpg', 3, 25, 1),
('Sombra Mono Gold', 'Sombra individual con brillo metálico dorado', 6.99, 'img/sombra_mono1.jpg', 3, 60, 0),
('Rímel Volume Max', 'Máscara de pestañas para efecto máximo volumen', 13.99, 'img/rimel1.jpg', 4, 55, 1),
('Rubor Peach Glow', 'Rubor en polvo con tono durazno natural', 11.99, 'img/rubor1.jpg', 5, 40, 0),
('Rubor Cream Rosy', 'Rubor en crema para look fresco y natural', 10.99, 'img/rubor2.jpg', 5, 35, 1),
('Iluminador Luna', 'Iluminador líquido con destellos perlados', 15.99, 'img/iluminador1.jpg', 6, 30, 1),
('Contour Kit Pro', 'Kit completo de contouring con 6 tonos', 22.99, 'img/contour1.jpg', 6, 20, 0),
('Serum Vitamina C', 'Serum facial antioxidante con vitamina C pura', 19.99, 'img/serum1.jpg', 7, 45, 1),
('Crema Hidratante Rose', 'Crema hidratación profunda con extracto de rosa', 16.99, 'img/crema1.jpg', 7, 50, 0),
('Set de Brochas Premium', 'Set de 10 brochas profesionales de maquillaje', 29.99, 'img/brochas1.jpg', 8, 15, 1),
('Esponja Beauty Blend', 'Esponja de maquillaje para base y corrector', 8.99, 'img/esponja1.jpg', 8, 70, 0),
('Fragancia Rose Garden', 'Eau de parfum con notas de rosa y peonía', 34.99, 'img/fragancia1.jpg', 9, 25, 1),
('Fragancia Midnight', 'Eau de parfum con notas intensas y duraderas', 39.99, 'img/fragancia2.jpg', 9, 20, 0);

INSERT INTO cupones (codigo, descuento, tipo, min_compra, fecha_expiracion) VALUES
('BIENVENIDO10', 10.00, 'porcentaje', 0.00, '2026-12-31'),
('ROSE20', 20.00, 'porcentaje', 25.00, '2026-12-31'),
('DESCUENTO5', 5.00, 'fijo', 15.00, '2026-12-31');
