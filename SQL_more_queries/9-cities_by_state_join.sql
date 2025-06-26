-- Script to list all cities with their states from hbtn_0d_usa database
-- Usage: mysql hbtn_0d_usa < list_all_cities.sql

SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
