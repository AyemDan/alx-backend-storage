-- Task: Create a 'users' table with 'id', 'email', 'name', and 'country' attributes
-- 'id' is an auto-incremented integer, 'email' is unique and cannot be null,
-- 'name' is optional, and 'country' is an enumeration with a default of 'US'.

-- Create the table 'users' if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- 'id' is auto-incremented and the primary key
    email VARCHAR(255) NOT NULL UNIQUE,          -- 'email' is unique and cannot be NULL
    name VARCHAR(255),                           -- 'name' is optional
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  -- 'country' is an ENUM with default 'US'
);
