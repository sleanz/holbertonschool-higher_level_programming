-- Script to list all cities of California from hbtn_0d_usa database
-- Usage: mysql hbtn_0d_usa < list_california_cities.sql

SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
