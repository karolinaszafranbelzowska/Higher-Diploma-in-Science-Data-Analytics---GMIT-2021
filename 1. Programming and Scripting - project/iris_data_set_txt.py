# Karolina Szafran-Belzowska, 2019/04/15
# iris flower data analysis

# this code will print the whole Fisher's iris flower data (from .txt file)

import numpy as np
import matplotlib.pyplot as plt 

data = np.genfromtxt('irisdata.txt', delimiter=',')


print(data)
