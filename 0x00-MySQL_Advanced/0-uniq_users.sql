-- SQL script to create the 'users' table
-- This script creates a table called 'users' with the following columns:
-- 1. id: an integer that is never null, auto-incremented, and set as the primary key
-- 2. email: a string (VARCHAR) of 255 characters, never null, and must be unique
-- 3. name: a string (VARCHAR) of 255 characters

-- Check if the table 'users' already exists, if not, create it
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
