# solution to problem 1
# Karolina Szafran Belzowska, 2021
# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

# Version # 1 (error)


input("Enter a positive integer to get the sum of all numbers between 1 and 10:")

print(int("1") + int("2") + int("3") + int("4") + int("5") + int("6") + int("7") + int("8") + int("9") + int("10"))

# =========================================================================================================

# Version # 2 (correct)


# Asks the user to input a positive integer number 

i = int(input("Please enter a positive integer: "))

# This will prevent the user from entering anything other than a positive integer.
# The message will print when the user types a negative integer.
if i <= 0: 
  print("Unfortunately this is not a positive integer. Please, try again.")

total = 0 

while i > 0:  # a while loop 
    total = total + i
    i = i - 1
    
# While 'i' is greater than 0 add the total and the current value of "i" and overwrite the current total. 

# i = i - 1: If the user inputs the positive integer of 10, the program subtracts one from the current value and so on, down to 0.
 
print(total)