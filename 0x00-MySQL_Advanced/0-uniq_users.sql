-- SQL script that creates a table users
USE `holberton`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `email` VARCHAR(255) UNIQUE,
  `name` VARCHAR(255)
);
