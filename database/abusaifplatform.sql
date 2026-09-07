-- Create the database
CREATE DATABASE IF NOT EXISTS abusaifplatform
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Select the database
USE abusaifplatform;

-- Create the admin table
CREATE TABLE IF NOT EXISTS admin (
    userid VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (userid)
);

-- Create the default administrator account
INSERT INTO admin (userid, password)
VALUES ('admin', 'password');