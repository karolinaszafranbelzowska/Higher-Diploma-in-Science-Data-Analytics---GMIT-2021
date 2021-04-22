# Karolina Szafran-Belzowska, 2019/03/18
# a plot of the funkction x to the power of 2 
# This video helped me to solve the problem https://www.youtube.com/watch?v=CuuvojEKHWo&t=202s

import matplotlib.pyplot as plt 

x =[i for i in range(0,4)]
y = [i**2 for i in x]
plt.plot (x,y)
plt.show()
