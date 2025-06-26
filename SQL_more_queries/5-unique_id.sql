-- Script to create unique_id table
-- Usage: mysql [database_name] < create_unique_id_table.sql

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
