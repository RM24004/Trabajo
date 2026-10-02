<?php
require_once __DIR__ . '/../config/database.php';

class Review {
    private $db;

    public function __construct() {
        $this->db = getConnection();
    }

    public function getByMovie($movieId) {
        $sql = "SELECT r.*, u.username FROM reviews r
                JOIN users u ON r.user_id = u.id
                WHERE r.movie_id = ?
                ORDER BY r.created_at DESC";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$movieId]);
        return $stmt->fetchAll();
    }

    public function getByUser($userId) {
        $sql = "SELECT r.*, m.title as movie_title, m.poster_url
                FROM reviews r
                JOIN movies m ON r.movie_id = m.id
                WHERE r.user_id = ?
                ORDER BY r.created_at DESC";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$userId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $sql = "SELECT r.*, u.username, m.title as movie_title
                FROM reviews r
                JOIN users u ON r.user_id = u.id
                JOIN movies m ON r.movie_id = m.id
                WHERE r.id = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function hasUserReviewed($userId, $movieId) {
        $stmt = $this->db->prepare("SELECT id FROM reviews WHERE user_id = ? AND movie_id = ?");
        $stmt->execute([$userId, $movieId]);
        return (bool)$stmt->fetch();
    }

    public function create($userId, $movieId, $rating, $title, $comment) {
        $sql = "INSERT INTO reviews (user_id, movie_id, rating, title, comment) VALUES (?, ?, ?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$userId, $movieId, $rating, $title, $comment]);
        return $this->db->lastInsertId();
    }

    public function update($id, $rating, $title, $comment) {
        $sql = "UPDATE reviews SET rating=?, title=?, comment=? WHERE id=?";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([$rating, $title, $comment, $id]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM reviews WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function getRecent($limit = 10) {
        $sql = "SELECT r.*, u.username, m.title as movie_title, m.poster_url
                FROM reviews r
                JOIN users u ON r.user_id = u.id
                JOIN movies m ON r.movie_id = m.id
                ORDER BY r.created_at DESC
                LIMIT ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$limit]);
        return $stmt->fetchAll();
    }

    public function countAll() {
        return $this->db->query("SELECT COUNT(*) FROM reviews")->fetchColumn();
    }
}
