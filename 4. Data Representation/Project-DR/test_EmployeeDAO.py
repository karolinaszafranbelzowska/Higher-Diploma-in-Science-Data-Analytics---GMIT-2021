# Karolina Szafran-Belzowska, G00376368 
# Data Representation and Quering, Higher Diploma In Data Analytics at GMIT, project 2020

# print("ok!") # print ok to see if everything works / and it works!

from EmployeeDAO import employeeDAO

person = {
    'employee_ID': 123,
    'employee_Name': 'John',
    'employee_Dept_ID': 123,
    'employee_Salary': 350.00
}

person2 = {
    'employee_ID': 124,
    'employee_Name': 'Mary',
    'employee_Dept_ID': 123,
    'employee_Salary': 370.00
}
# returnValue = employeeDAO.create(person)  # works
# returnValue = employeeDAO.create(person2) 
# print (returnValue)

# print("Find By ID")
returnValue =  employeeDAO.findById('employee_ID') 
print (returnValue)

# returnValue =  employeeDAO.findById(person2['employee_ID']) 
# print (returnValue)

# returnValue =  employeeDAO.update(person2) 
# print (returnValue)

# returnValue =  employeeDAO.findById(person2['employee_ID']) 
# print (returnValue)

# returnValue =  employeeDAO.delete(person2['employee_ID']) 
# print (returnValue)

returnValue =  employeeDAO.getAll() 
print (returnValue)




