# Student Management System

A Python-based CRUD application to manage student records using MySQL.

## Features
- Add new student records
- View all students
- Update student details
- Delete student records

## Technologies Used
- Python
- MySQL

## Description
This project is a simple command-line based application developed using Python.
It performs basic CRUD operations (Create, Read, Update, Delete) on student data
stored in a MySQL database.

This project is intended for learning backend logic and database integration.

## How to Run the Project

1. Install Python (version 3.8 or above)
2. Install MySQL and start the MySQL server
3. Install required package:
   pip install mysql-connector-python
4. Open terminal or command prompt
5. Run the program:
   python main.py

## Database Setup

1. Create a MySQL database:
   CREATE DATABASE student_management;

2. Use the database:
   USE student_management;

3. Create the student table:
   CREATE TABLE students (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(100),
       age INT,
       course VARCHAR(100)
   );
