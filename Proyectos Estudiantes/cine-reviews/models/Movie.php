<?php
require_once __DIR__ . '/../config/database.php';

class Movie {
    private $db;

    public function __construct() {
        $this->db = getConnection();
    }

    public function getAll($search = '', $genre = '', $order = 'newest') {
        $sql = "SELECT * FROM movies WHERE 1=1";
        $params = [];

        if ($search) {
            $sql .= " AND (title LIKE ? OR director LIKE ?)";
            $params[] = "%$search%";
            $params[] = "%$search%";
        }
        if ($genre) {
            $sql .= " AND genre = ?";
            $params[] = $genre;
        }

        switch ($order) {
            case 'rating': $sql .= " ORDER BY rating_avg DESC"; break;
            case 'year': $sql .= " ORDER BY release_year DESC"; break;
            default: $sql .= " ORDER BY created_at DESC";
        }

        $stmt = $this->db->prepare($sql);
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM movies WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $sql = "INSERT INTO movies (title, synopsis, director, release_year, genre, poster_url) VALUES (?, ?, ?, ?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([
            $data['title'], $data['synopsis'], $data['director'],
            $data['release_year'], $data['genre'], $data['poster_url'] ?? null
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $sql = "UPDATE movies SET title=?, synopsis=?, director=?, release_year=?, genre=?, poster_url=? WHERE id=?";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([
            $data['title'], $data['synopsis'], $data['director'],
            $data['release_year'], $data['genre'], $data['poster_url'] ?? null, $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM movies WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function updateRating($movieId) {
        $sql = "UPDATE movies SET rating_avg = (SELECT COALESCE(ROUND(AVG(r.rating), 2), 0) FROM reviews r WHERE r.movie_id = ?) WHERE id = ?";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([$movieId, $movieId]);
    }

    public function getGenres() {
        $stmt = $this->db->query("SELECT DISTINCT genre FROM movies ORDER BY genre");
        return $stmt->fetchAll(PDO::FETCH_COLUMN);
    }

    public function getTopRated($limit = 5) {
        $stmt = $this->db->prepare("SELECT * FROM movies ORDER BY rating_avg DESC LIMIT ?");
        $stmt->execute([$limit]);
        return $stmt->fetchAll();
    }

    public function countAll() {
        return $this->db->query("SELECT COUNT(*) FROM movies")->fetchColumn();
    }
}
