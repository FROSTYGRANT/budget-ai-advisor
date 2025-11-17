-- Run this in your MySQL shell or Workbench
CREATE DATABASE IF NOT EXISTS budget_app;
USE budget_app;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);