-- Run this file once in MySQL to create the database and table.
-- Sayan Sir's Tutorials (CoE Kolkata)

CREATE DATABASE IF NOT EXISTS school_db;
USE school_db;

CREATE TABLE IF NOT EXISTS students (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    roll_no INT NOT NULL UNIQUE,
    name    VARCHAR(50) NOT NULL,
    section CHAR(1) NOT NULL,
    stream  VARCHAR(20) NOT NULL,
    marks   INT NOT NULL
);

-- A few sample records to start with
INSERT INTO students (roll_no, name, section, stream, marks) VALUES
(1, 'Aarav Sen',     'A', 'Science',    88),
(2, 'Riya Das',      'A', 'Commerce',   92),
(3, 'Sourav Ghosh',  'B', 'Humanities', 76),
(4, 'Ananya Roy',    'B', 'Science',    95);

SELECT * FROM students;
