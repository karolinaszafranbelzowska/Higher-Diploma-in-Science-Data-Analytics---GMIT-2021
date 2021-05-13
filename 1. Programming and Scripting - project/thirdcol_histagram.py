# Karolina Szafran-Belzowska, 2019/04/27
# Iris Flower Data Analysis

# third column histogram (petal length)

import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('irisdata.txt', delimiter=',')
thirdcol = data[:,2]
meanthirdcol = np.mean(data[:,2])

print(meanthirdcol)


pl.hist(thirdcol)
pl.show()
