![](images/logo_GMIT.jpeg)

## Higher Diploma in Data Analytics
### Karolina Szafran-Belzowska, G00376368


A conversion course for graduates of level 8 programmes in disciplines other than computing, the aim of this programme is to provide students with a broad knowledge of computing, 
with a specialisation in data analytics. 
This will enable students to apply data analysis techniques to the topics in their original degree, while also providing a foundation on which they can develop their skills in 
the more traditional areas of computing. 
The course covers such skills as automating manual spreadsheet-oriented data analysis processes, converting large data sets into actionable information, and creating web-based 
dashboards for visualising data. 
Level 8 graduates from disciplines such as business and finance are particularly suited to this course, as are those from life and physical sciences.


### Modules
________________________________________

1. Programming and Scripting	(10 credits)
2. Computational Thinking with Algorithms	(5 credits)
3. Computer Architecture and Technology Convergence	(5 credits)
4. Data Representation	(5 credits)
5. Fundamentals of Data Analysis	(5 credits)
6. Programming for Data Analysis	(10 credits)
7. Applied Databases	(5 cedits)
8. Web Application Development	(5 credits)
9. Machine Learning and Statistics	(5 credits)
10. Multi-paradigm programming	(5 credits)
11. Work Placement or Project	(15 credits)


### Learning outcomes
________________________________________
The learner will have knowledge and understanding of advanced concepts in the following areas.
1.	Data analysis: collecting, cleaning, processing, exploring and modelling.
2.	Programming: iteration, conditions, abstraction, procedures.
3.	Mathematical foundations: numerical software, regression, hypothesis testing.
4.	Professional issues: summarisation of results, presentation, decision making.

The learner will be able to:
1.	Identify real-world problems that are well suited to data analysis; Recognise, understand and appreciate techniques in computational data analytics; Describe the limitations of current techniques and technologies in computing and data analytics.
2.	Model real world problems from a data analytics perspective; Design and construct a data analytics workflow to solve a data-intensive computational problem; Identify, analyse and plan strategies for solving general computational problems.
3.	Identify and select appropriate data analysis techniques in a range of real-world contexts; Apply quality concepts to computer programming and data analytics workflows; Manage a computer-based project throughout all stages of its lifecycle.
4.	Apply best practice in the fields of computing and data analytics; Apply diagnostic skills in a range of data-focused contexts; Discuss, plan and implement fundamental techniques in computing, including programming.
5.	Work autonomously in solving problems using a computer; Plan and track the development of software by a group of people; Recognise the different roles involved in organising a project in data analysis.
6.	Locate and evaluate documentation and information through online research; Assimilate new skills and techniques in computing through online learning; Criticise computational work in a constructive manner.
7.	Critique the ways in which data analysis affects the world; Summarise how academic and industrial research leads to new knowledge, solutions and techniques in data analysis; Recommend an appropriate course of action based on results from data analysis.

 
### 1. Programming and Scripting
________________________________________
This module is an introduction to automating computer tasks using scripting languages and solving problems using programming languages, with a focus on
data. It covered the high-level concepts and the theory.

#### Learning Outcomes

1. Automate computer tasks using a scripting language.
2. Write configuration files for a variety of software applications.
3. Setup and configure a software development environment and toolchain.
4. Develop an algorithm to solve a computational problem.
5. Write a computer program in a high-level programming language.
6. Construct a complex computer program from a series of simpler computer programs

#### How download this repository

1. Go to Github and select Programming and Sripting - Jupyter notebook or Programming and Scripting - VSC.
2. Click the download button.

#### How to run the code

1. Make sure you have Python installed. https://www.python.org/downloads/
2. Download Python using Anaconda and use iPython. https://www.anaconda.com/distribution/
3. Anaconda allows you to use software such as Visual Studio Code. https://code.visualstudio.com/download
5. Download Vivual Studio Code, this will assist you in saving annd editing your code.
6. Install Cmder in Windows to allow you run the code used in this repository. https://cmder.net/
7. Open a command winder and use ipython.


### 2. Computational Thinking with Algorithms
________________________________________

This repository contains the benchmarking code for five different sorting algorithms as part of the assessment in the Computational Thinking with Algorithms module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

The module covers a comprehensive foundation in computational problem solving and algorithm design. 

### Learning Outcomes
1. Apply structured methodologies to problem solving in computing.
2. Design algorithms to solve computational problems.
3. Critically evaluate and assess the performance of algorithms.
4. Translate real-world problems into computational problems

### Project Description
This project implements functions for and benchmarks five sorting algorithms:

- Bubble Sort,
- Counting Sort,
- Insertion Sort,
- Merge Sort,
- Selection Sort

The benchmarking process begins with the creation of arrays of random integer arrays of increasing size, each of which are passed to all of the sorting functions. The sorting functions are timed with each array ten times to get an average time for each input size and the results are collated in a dataframe. 

It should be noted that due to the nature of the simple sorting algorithms, the code herein may take quite some time to run as they attempt to sort the larger input sizes.

#### How to run 'Jupyter notebook'
The Jupyter Notebook App can be launched by clicking on the Jupyter Notebook icon installed by Anaconda in the start menu (Windows) or by typing in a terminal (cmd on Windows):
'jupyter notebook'

This will launch a new browser window (or a new tab) showing the Notebook Dashboard, a sort of control panel that allows (among other things) to select which notebook to open. Taken from: Jupyter notebook

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.


### 3. Computer Architecture and Technology Convergence
________________________________________

This repository contains the assessment in the Computer Architecture and Technology Convergence module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

The module introduces you to the inner workings, structure, architecture and organization of modern computer architectures.

The project is written using a standard word processor and .pdf format.

#### Learning Outcomes

1. Demonstrate an understanding of the components in modern computer architectures.
2. Troubleshoot common computer hardware and software problems.
3. Describe the topologies of computer networks.
4. Explain the role of abstraction in the development of computer hardware and software.


### 4. Data Representation
________________________________________

This repository contains the assignment of the Data Representation module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

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
DAO stands for Data Access Object. The EmployeeDAO.py file consists of a number of functions which access the database and perform CRUD operations. It is a pattern that provides an abstract interface to some type of database or other persistence mechanism. The DAO provides some specific data operations without exposing details of the database[1].

### How to run
At the command prompt: For those who do not have 'flask' and 'mysql-connector' installed:
```
pip install flask
pip install mysql-connector
```
In the command prompt type command: python server.py. to make the server running (at http://127.0.0.1:5000). In the browser address bar: http://127.0.0.1:5000/employee.html - starts the web interface that uses AJAX to perform database.

### MySQL database & table
Database = dr_project Table = employee

MySQL command to create employee table:
```
create table employee (
    employee_ID int NOT NULL PRIMARY KEY,
    employee_Name varchar(100),
    employee_Dept_ID int,
    employee_Salary int
);
```
