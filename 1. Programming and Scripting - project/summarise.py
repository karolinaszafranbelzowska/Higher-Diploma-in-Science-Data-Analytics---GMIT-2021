# Karolina Szafran Belzowska, 2019/04/25
# Iris Flower Data Analysis

# this code will print the Iris flower Data Set:
# mean, min., max., std., percentage and count.
# it will summarise the data 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = ('irisdata_project_2019.csv')
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width','species']
dataset = pd.read_csv(data, header=0)

print(dataset.describe())
