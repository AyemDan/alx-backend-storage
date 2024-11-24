-- Task: Create a 'users' table with 'id', 'email', and 'name' attributes

-- Create the table 'users' if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    -- 'id' is an auto-incremented integer, cannot be NULL, and is the primary key
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    -- 'email' is a string (255 characters), cannot be NULL, and must be unique
    email VARCHAR(255) NOT NULL UNIQUE,

    -- 'name' is a string (255 characters) and is optional (can be NULL)
    name VARCHAR(255)
);

