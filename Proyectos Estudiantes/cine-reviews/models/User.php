<?php
require_once __DIR__ . '/../config/database.php';

class User {
    private $db;

    public function __construct() {
        $this->db = getConnection();
    }

    public function register($username, $email, $password) {
        $hash = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $this->db->prepare("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)");
        return $stmt->execute([$username, $email, $hash]);
    }

    public function login($email, $password) {
        $stmt = $this->db->prepare("SELECT * FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();
        if ($user && password_verify($password, $user['password_hash'])) {
            return $user;
        }
        return false;
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT id, username, email, created_at FROM users WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function usernameExists($username) {
        $stmt = $this->db->prepare("SELECT id FROM users WHERE username = ?");
        $stmt->execute([$username]);
        return (bool)$stmt->fetch();
    }

    public function emailExists($email) {
        $stmt = $this->db->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->execute([$email]);
        return (bool)$stmt->fetch();
    }

    public function getUserStats($userId) {
        $stmt = $this->db->prepare("SELECT COUNT(*) as total_reviews FROM reviews WHERE user_id = ?");
        $stmt->execute([$userId]);
        $reviews = $stmt->fetch();

        $stmt = $this->db->prepare("SELECT ROUND(AVG(rating), 2) as avg_rating FROM reviews WHERE user_id = ?");
        $stmt->execute([$userId]);
        $avg = $stmt->fetch();

        return [
            'total_reviews' => $reviews['total_reviews'],
            'avg_rating' => $avg['avg_rating'] ?? 0
        ];
    }
}
