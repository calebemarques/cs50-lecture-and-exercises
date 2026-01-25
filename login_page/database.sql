CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample user data (passwords are hashed using SHA-256 for demo purposes)
-- Note: In a real application, use proper password hashing like bcrypt
INSERT INTO users (username, password_hash, email) VALUES
('admin', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'admin@example.com'),
('user1', 'b03ddf3ca2e714a6548e7495c2a03f5e824eaac9837cd7f159c67b90fb4b7342a', 'user1@example.com'),
('user2', '8d23cf6c86e834a7aa6eded54c26ce2bb2e74903538c61bdd5d2197997ab2f72', 'user2@example.com');

-- Create an index on username for faster lookups
CREATE INDEX idx_username ON users(username);
=======
-- SQL Database Schema for User Authentication
-- This file contains the SQL commands to create and populate the users table

-- Create the users table for storing login credentials
-- Includes fields for user ID, username, password hash, email, and creation timestamp
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incrementing primary key
    username TEXT UNIQUE NOT NULL,         -- Unique username for login
    password_hash TEXT NOT NULL,           -- Hashed password for security
    email TEXT,                            -- Optional email address
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Timestamp of account creation
);

-- Insert sample user data (passwords are hashed using SHA-256 for demo purposes)
-- Note: In a real application, use proper password hashing like bcrypt
-- These are demo accounts for testing the login functionality
INSERT INTO users (username, password_hash, email) VALUES
('admin', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'admin@example.com'),
('user1', 'b03ddf3ca2e714a6548e7495c2a03f5e824eaac9837cd7f159c67b90fb4b7342a', 'user1@example.com'),
('user2', '8d23cf6c86e834a7aa6eded54c26ce2bb2e74903538c61bdd5d2197997ab2f72', 'user2@example.com');

-- Create an index on username for faster lookups during login attempts
-- This improves performance when searching for users by username
CREATE INDEX idx_username ON users(username);
