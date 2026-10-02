CREATE DATABASE IF NOT EXISTS cine_reviews CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cine_reviews;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    avatar VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    synopsis TEXT NOT NULL,
    director VARCHAR(100) NOT NULL,
    release_year INT NOT NULL,
    genre VARCHAR(100) NOT NULL,
    poster_url VARCHAR(500) DEFAULT NULL,
    rating_avg DECIMAL(3,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(150) NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_movie (user_id, movie_id)
) ENGINE=InnoDB;

CREATE INDEX idx_movies_genre ON movies(genre);
CREATE INDEX idx_movies_year ON movies(release_year);
CREATE INDEX idx_reviews_movie ON reviews(movie_id);
CREATE INDEX idx_reviews_user ON reviews(user_id);

INSERT INTO users (username, email, password_hash) VALUES
('admin', 'admin@cinereviews.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi'),
('maria', 'maria@email.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi'),
('carlos', 'carlos@email.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi');

INSERT INTO movies (title, synopsis, director, release_year, genre, poster_url) VALUES
('El Padrino', 'La historia de la familia Corleone, una de las cinco familias que dominan el crimen organizado en Nueva York.', 'Francis Ford Coppola', 1972, 'Drama', 'https://via.placeholder.com/300x450?text=El+Padrino'),
('Inception', 'Un ladrón que roba secretos a traves de los suenos recibe una ultima tarea: sembrar una idea en la mente de un objetivo.', 'Christopher Nolan', 2010, 'Ciencia Ficcion', 'https://via.placeholder.com/300x450?text=Inception'),
('El Laberinto del Fauno', 'En la Espana franquista de 1944, una nina descubre un laberinto abandonado con un ser mitico.', 'Guillermo del Toro', 2006, 'Fantasia', 'https://via.placeholder.com/300x450?text=Laberinto+del+Fauno'),
('Pulp Fiction', 'Historias entrelazadas de crimen y redencion en el bajo mundo de Los Angeles.', 'Quentin Tarantino', 1994, 'Accion', 'https://via.placeholder.com/300x450?text=Pulp+Fiction'),
('Coco', 'Un nino mexico de 12 anos anhela ser musico y accidentalmente llega al mundo de los muertos.', 'Lee Unkrich', 2017, 'Animacion', 'https://via.placeholder.com/300x450?text=Coco');

INSERT INTO reviews (user_id, movie_id, rating, title, comment) VALUES
(1, 1, 5, 'Una obra maestra absoluta', 'La mejor pelicula jamas filmada. La actuacion de Marlon Brando es legendaria.'),
(2, 1, 5, 'Imprescindible del cine', 'Un clasico que todo amante del cine debe ver. La direccion es impecable.'),
(1, 2, 4, 'Mente retorcida', 'Nolan nos lleva por un viaje mental impresionante. El final te deja pensando.'),
(3, 3, 5, 'Magia oscura mexicana', 'Guillermo del Toro crea un mundo fantastico precioso y oscuro al mismo tiempo.'),
(2, 4, 5, 'Tarantino en su mejor momento', 'Dialogos brillantes y escenas inolvidables. El monologo de Vincent Vega es icónico.'),
(3, 5, 4, 'Lagrimas garantizadas', 'Una pelicula hermosa que celebra la cultura mexicana y la musica.'));

UPDATE movies m
SET rating_avg = (SELECT ROUND(AVG(r.rating), 2) FROM reviews r WHERE r.movie_id = m.id);
