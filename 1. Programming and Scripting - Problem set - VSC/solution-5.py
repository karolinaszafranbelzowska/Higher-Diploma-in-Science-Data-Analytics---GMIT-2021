# Karolina Szafran-Belzowska, 2019/03/16
# Adapted from https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops and 
# https://stackoverflow.com/questions/18833759/python-prime-number-checker
# This code will show the user wheter or not the number is a prime

# Karolina Szafran-Belzowska, 2019/03/16
# Adapted from https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops and 
# https://stackoverflow.com/questions/18833759/python-prime-number-checker
# This code will show the user wheter or not the number is a prime

i=int(input("Enter any possitive integer between 1 and 100:"))
if i <= 1:
    print("number is not prime")
else:
    a=2
    check = True
    while a != i:
        if i%a == 0:
            print("Number is not prime")
            check = False
            break
        a+=1
    if check == True:
        print("Number is prime")
