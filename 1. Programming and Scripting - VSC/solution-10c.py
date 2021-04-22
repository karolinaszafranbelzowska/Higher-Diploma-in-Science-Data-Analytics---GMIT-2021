# Karolina Szafran-Belzowska, 2019/03/18
# a plot of the funkction 2 to the power of x

import matplotlib.pyplot as plt 

x =[i for i in range(0,4)]
y = [2**i for i in x]
plt.plot (x,y)
plt.show()
