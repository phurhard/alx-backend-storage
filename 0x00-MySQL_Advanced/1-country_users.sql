-- Creates a table named users with attr of name, email and country

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VAR(255) NOT NULL UNIQUE,
    name VAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
