# Karolina Szafran-Belzowska, 2019/04/27
# Iris Flower Data Analysis

# fourth column histogram (petal width)

import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('irisdata.txt', delimiter=',')
fourthcol = data[:,3]
meanfourthcol = np.mean(data[:,3])

print(meanfourthcol)


pl.hist(fourthcol)
pl.show()

