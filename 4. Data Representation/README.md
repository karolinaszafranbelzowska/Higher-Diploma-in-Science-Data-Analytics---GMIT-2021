# GMIT Data Representation Module Project 2020.
## Higher Diploma in Data Analytics, Lecturer: Andrew Beatty
### Karolina Szafran-Belzowska, G00376368

This project has been carried out as an assignment of the Data Representation module of the Higher Diploma In Data Analytics at GMIT.

### The repository contains:


- README.md file
- .gitignore
- requirements.txt - stores required packages 
- mySQL database
- Python 'DAO' programme to access the mySQL database, this programme consumes an API. (EmployeeDAO.py, testEmployeeDAO.py- it was used to test the DAO.)
- Python 'application' to run a Flask server (server.py) in a virtual enviroment
- createDBproject.py - code to create the database ('dr_project')
- employee.html page 
- employee.png


### AJAX
A technique of creating web applications in which user interaction with the server takes place without reloading the entire document, in an asynchronous manner. This is to allow more dynamic interaction with the user than in the traditional model where every word applies to all HTML pages[2].
### DAO
DAO stands for Data Access Object. The EmployeeDAO.py file consists of a number of functions which access the database and perform CRUD operations. 
It is a pattern that provides an abstract interface to some type of database or other persistence mechanism. The DAO provides some specific data operations without exposing details of the database[1].

### How to run
At the command prompt: For those who do not have 'flask' and 'mysql-connector' installed:
```
pip install flask
pip install mysql-connector
```
In the command prompt type command: *python server.py*. to make the server running (at http://127.0.0.1:5000).
In the browser address bar: http://127.0.0.1:5000/employee.html - starts the web interface that uses AJAX to perform database.

### MySQL database & table
Database = dr_project
Table = employee

MySQL command to create employee table:
```
create table employee (
    employee_ID int NOT NULL PRIMARY KEY,
    employee_Name varchar(100),
    employee_Dept_ID int,
    employee_Salary int
);
```







### References
[1] https://en.wikipedia.org/wiki/Data_access_object, 05/12/2020

[2] https://pl.wikipedia.org/wiki/AJAX, 08/12/2020

[3] https://www.w3schools.com/xml/ajax_intro.asp,08/12/2020

https://github.com/andrewbeattycourseware/dataRepresenation2020

GMIT Video Lectures, Andrew Beatty
