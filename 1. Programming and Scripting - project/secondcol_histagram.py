# Karolina Szafran-Belzowska, 2019/04/27
# Iris Flower Data Analysis

# second column histogram (sepal width)

import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('irisdata.txt', delimiter=',')
secondcol = data[:,1]
meansecondcol = np.mean(data[:,1])

print(meansecondcol)


pl.hist(secondcol)
pl.show()

