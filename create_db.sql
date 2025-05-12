DROP TABLE IF EXISTS usage;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS plans;

CREATE TABLE plans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    permissions JSON NOT NULL,
    usage_limits JSON NOT NULL
);

CREATE TABLE permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    api_endpoint VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE subscriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    plan_id INT,
    FOREIGN KEY (plan_id) REFERENCES plans(id)
);
CREATE TABLE usage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    api_name VARCHAR(255) NOT NULL,
    count INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES subscriptions(user_id)
);