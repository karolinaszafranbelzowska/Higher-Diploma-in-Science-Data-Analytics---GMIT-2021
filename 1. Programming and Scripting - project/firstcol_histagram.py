# Karolina Szafran-Belzowska, 2019/04/27
# Iris Flower Data Analysis

# first column histogram (sepal length)


import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('irisdata.txt', delimiter=',')
firstcol = data[:,0]
meanfirstcol = np.mean(data[:,0])

print(meanfirstcol)


pl.hist(firstcol)
pl.show()
