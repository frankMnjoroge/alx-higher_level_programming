-- script that creates the database hbtn_0d_usa
-- creates table states with attributes id INT unique, auto generated, can’t be null
-- and is a primary key name VARCHAR(256) can’t be not be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
