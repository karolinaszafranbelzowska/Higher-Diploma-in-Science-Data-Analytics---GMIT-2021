# Karolina Szafran-Belzowska, 25/10/2020
# Write a Python function that calculates and prints 
# to the screen the square root of 2 to 100 decimal places.


# In this example I used Mathematical function


# 1st example
import math # imported math function
print(math.sqrt(2)) # print the square root of 2


#2nd example
import math
a = 2
root = (format(math.sqrt(a), '.100f'))
print('The square root of a is: ' + repr(root))


#3rd example
from sympy import sqrt # import sympy, sqrt method
print('The square root of a to 100 decimal places is: ')
print(sqrt(2).evalf(100)) # .evalf() method will print a partially evaluated expression.



# References:
# https://www.geeksforgeeks.org/python-sympy-sqrt-method-2/ 25/10/2020
# https://pl.coredump.biz/questions/4733173/how-can-i-show-an-irrational-number-to-100-decimal-places-in-python#4733238 25/10/2020
# https://realpython.com/python-square-root-function/ 25/10/2020
# https://docs.python.org/3/library/math.html 25/10/2020
# https://docs.sympy.org/latest/modules/simplify/simplify.html 25/10/2020


# For the purpose of the Machine Learning and STatistics task my code
# should not depend on any module from the standard library or otherwise.


