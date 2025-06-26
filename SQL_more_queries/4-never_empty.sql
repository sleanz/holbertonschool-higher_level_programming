-- Script to create id_not_null table
-- Usage: mysql [database_name] < create_id_not_null_table.sql

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
