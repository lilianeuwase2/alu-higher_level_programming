-- This script creates the table id_not_null on MySQL server
-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);