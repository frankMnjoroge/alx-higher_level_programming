-- script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates table states with attributes id INT unique, auto generated, can’t be null
-- and is a primary key name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS `state` (id INT UNIQUE NOT NULL AUTO_INCREAMENT,name VARCHAR(256) NOT NULL, PRIMARY KEY(id)); 
