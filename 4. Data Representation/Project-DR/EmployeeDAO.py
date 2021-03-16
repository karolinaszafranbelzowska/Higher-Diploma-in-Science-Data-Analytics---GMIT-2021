# Karolina Szafran-Belzowska, G00376368 
# Data Representation and Quering, Higher Diploma In Data Analytics at GMIT, project 2020

import mysql.connector # pip install mysql-connector

# Code taken from https://github.com/andrewbeattycourseware/dataRepresenation2020, 05/12/2020

# create a class EmployeeDAO to contain all functions
class EmployeeDAO:
    db = ""       # variable stores database connection
    def __init__(self): 
        self.db = mysql.connector.connect (   # will open a connection to a MySQL server and return a MySQLConnection object.
            host = 'localhost',
            user = 'root',
            password = '25Szarfa',
            database = 'dr_project'
        )
# print("Connection made") # check if connection is made / works!

# Function called 'create'
    def create(self, person):
        cursor = self.db.cursor()
        sql = "Insert into employee(employee_ID, employee_Name, employee_Dept_ID, employee_Salary) values (%s,%s,%s,%s)"
        values = [
            person['employee_ID'],
            person['employee_Name'],
            person['employee_Dept_ID'],
            person['employee_Salary']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

# Function called 'getAll'
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from employee'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results) / # works

        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray
    
# Function called 'findById' - find One    
    def findById(self, employee_ID):
        cursor = self.db.cursor()
        sql = 'select * from employee where employee_ID = %s'
        values = [ employee_ID ]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        # return {}

# Function called 'update' 
    def update(self, person):
        cursor = self.db.cursor()
        sql = "update employee set employee_Name = %s, employee_Dept_ID = %s, employee_Salary = %s where employee_ID = %s"
# It is important to keep the order.
        values = [
           person['employee_Name'],
           person['employee_Dept_ID'],
           person['employee_Salary'],
           person['employee_ID']
       ]
        cursor.execute(sql, values)
        self.db.commit()
        return person

# Function called 'delete'
    def delete(self, employee_ID):
        cursor = self.db.cursor()
        sql = 'delete from employee where employee_ID = %s'
        values = [employee_ID]
        cursor.execute(sql, values)
        return {}

# Function called 'convertToDict'
    def convertToDict(self,result):
        colnames= ['employee_ID', 'employee_Name','employee_Dept_ID','employee_Salary']
        person = {}
        
        if result:
            for i, colName in enumerate(colnames):
                 value = result[i]  # extract from the dict object
                 person[colName]= value # make the person that matches the column

        return person



employeeDAO = EmployeeDAO()