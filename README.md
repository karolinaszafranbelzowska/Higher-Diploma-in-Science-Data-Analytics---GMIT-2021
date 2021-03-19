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


### Learning outcomes:
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
This module in which I was investigating and operating the protocols, standards and architectures used in representing data, with a focus on
interacting with data services across the Internet. I also gained practical experience in developing applications that interact with such data.

#### Learning Outcomes: (https://www.gmit.ie/sites/default/files/public/computing/docs/data-representation.pdf)
1. Compare data models and architectures used in applications.
2. Write software applications that adhere to common standards and protocols.
3. Explain the basic mechanisms by which application data is transmitted across the internet.
4. Design and utilise application programming interfaces for interacting with data sources.

#### The repository contains:
- README.md file
- .gitignore
- requirements.txt - stores required packages
- mySQL database
- Python 'DAO' programme to access the mySQL database, this programme consumes an API. (EmployeeDAO.py, testEmployeeDAO.py- it was used to test the DAO.)
- Python 'application' to run a Flask server (server.py) in a virtual enviroment
- createDBproject.py - code to create the database ('dr_project')
- employee.html page
- employee.png

#### AJAX
A technique of creating web applications in which user interaction with the server takes place without reloading the entire document, in an asynchronous manner. This is to allow more dynamic interaction with the user than in the traditional model where every word applies to all HTML pages.

#### DAO
DAO stands for Data Access Object. The EmployeeDAO.py file consists of a number of functions which access the database and perform CRUD operations. It is a pattern that provides an abstract interface to some type of database or other persistence mechanism. The DAO provides some specific data operations without exposing details of the database.

#### How to run
At the command prompt: For those who do not have 'flask' and 'mysql-connector' installed:
```
pip install flask
pip install mysql-connector
```
In the command prompt type command: python server.py. to make the server running (at http://127.0.0.1:5000). In the browser address bar: http://127.0.0.1:5000/employee.html - starts the web interface that uses AJAX to perform database.

#### MySQL database & table
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

### 5. Fundamentals of Data Analysis
________________________________________

![](images/tips.jpg)

This repository contains my assessment for the module "Fundamentals of Data Analysis" at Galway-Mayo Institute of Technology. 

The module Fundamentals of Data Analysis is an introduction to the fundamentals of data analysis, including the acquisition, cleaning and exploration of data sets.

#### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/fundamentals-data-analysis.pdf
1. Source and investigate sets of data.
2. Programmatically explore and visualise data.
3. Apply basic mathematical data analysis techniques to data sets.
4. Write programs to automate basic data analysis techniques.

#### Attribute information of the project:
- Total_bill in $,
- Tip in $,
- Sex of tipper: Female or Male,
- Smoker: Yes or No,
- Day: Thursday to Sunday,
- Meal: Lunch or Dinner,
- and size of the table.

#### How to run the project
Make sure you have Python installed. The project is written in Jupyter notebook and it is called "Fundamentals of Data Analysis - tips dataset.ipynb", where the Data is summarized. The project also contains "tipsdata.csv" and "tips.jpg" (file with Photo of TIPS).

#### How to run the Jupyter notebook
The Jupyter Notebook App can be launched by clicking on the Jupyter Notebook icon installed by Anaconda in the start menu (Windows) or by typing in a terminal (cmd on Windows):
```
jupyter notebook
```
This will launch a new browser window (or a new tab) showing the Notebook Dashboard, a sort of control panel that allows (among other things) to select which notebook to open. Taken from: Jupyter notebook.

### 6. Programming for Data Analysis
________________________________________

![](images/data_science.jpeg)

This module develops programming skills towards the effective use of data analysis libraries and software.
I have learnt how to select efficient data structures for numerical programming, and to use these data structures to transform
data into useful and actionable information.

#### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/programming-data-analysis.pdf

1. Perform exploratory analysis on data.
2. Programmatically create plots and other visual outputs from data.
3. Design computer algorithms to solve numerical problems.
4. Create software that incorporates and utilises standard numerical libraries.
5. Employ appropriate data structures when programming for data-intensive applications.
6. Model real-world, data-intensive problems as computing problems.

This assignment on numpy.random is the part of the Programming for Data Analysis 2019 module at Galway-Mayo Institute of Technology. It contains the numpy.random package in Python. In this assignment I tried to explain in details the use of the numpy.random package in Python using explanations and examples. I created a jupyter notebook and use this to show examples of numpy.random and its uses.

#### There are 4 main sections in this assignment
1. Explain the overall use of the numpy.random package.
2. Explain the use of the "Simple random data" and Permutations" functions.
3. Explain the use and purpose of at least five "Distributions" functions.
4. Explain the use of seeds in generating pseudorandom numbers.

### 7. Applied Database
________________________________________

![](images/big_data.jpeg)

This module is a comprehensive primer on databases, with a focus on data analysis. The creation, retrieval, update and deletion of both structured and
unstructured data will be covered for a number of modern database systems and architectures.

### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/applied-databases.pdf
1. Create, retrieve, update and delete data in a variety of modern database management systems.
2. Determine the correct data to select from a database in order to perform a given data analysis.
3. Select an appropriate interface to access a database for a given application.
4. Determine the best balance between application and database logic for a given data analysis process.

### 8. Web Application Development
________________________________________
![](images/web_application.jpg)

This module introduced to modern web application and network application development using frameworks in high-level
programming and scripting languages. The focus was on building light-weight network services, particularly web-based services, and integrating
those services with modern front-end frameworks.

#### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/web-application-development.pdf
1. Describe the common architectures of web applications.
2. Create scalable web services using modern architectural patterns.
3. Create a web application using a server-side framework.
4. Manage the development of a web application.

### 9. Machine Learning and Statistics
________________________________________
![](images/machine_learning.jpeg)

This module was an introduction to machine learning and the statistical aspects surrounding the theory.

#### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/machine-learning-statistics.pdf
1. Describe the stochastic nature of real-world measurements.
2. Select an appropriate mathematical model of a real-world problem.
3. Select an appropriate cost function for a given machine learning task.
4. Apply an optimisation technique to the parameters of a model.

### 10. Multi-paradigm programming
________________________________________
![](images/paradigm.jpeg)

This module was an introduction to various programming paradigms, such as object-oriented programming, functional programming and dataflow
programming.

#### Learning Outcomes https://www.gmit.ie/sites/default/files/public/computing/docs/multi-paradigm-programming.pdf
1. Compare different programming paradigms.
2. Select an appropriate programming paradigm for a given programming problem.
3. Write programs using a variety of different programming paradigms.
4. Explain how various programming paradigms have evolved over time.



### How to clone any repository
1. Go to GitHub.
2. Go to my repository: https://github.com/karolinaszafranbelzowska/Higher-Diploma-in-Science-Data-Analytics---GMIT-2021
3. Click the Code button which is colored green.
4. Click on HTTPS and copy the link that is shown.
5. Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
6. Enter the command: git clone followed by the URL of the repository.
7. The repository will be cloned down to your current working directory.
8. You will need to navigate to this folder location on the command line in order to run the program.
