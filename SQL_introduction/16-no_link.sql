-- Script to list all records from second_table excluding rows where name is NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
