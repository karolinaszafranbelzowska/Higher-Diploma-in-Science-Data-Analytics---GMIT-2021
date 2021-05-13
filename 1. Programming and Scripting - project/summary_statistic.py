# Karolina Szafran-Belzowska, 2019/04/28
# Iris Flower Data Analysis

# this code will print the Iris flower Data Set:
# mean, min., max., std., percentage and count.
# it will summarise the data 

import numpy as np
import pandas as pd

iris_data = pd.read_csv('irisdata_project_2019.csv')

summary = iris_data.describe()
summary = summary.transpose()
print(summary.head())