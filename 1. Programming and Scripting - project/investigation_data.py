# Karolina Szafran-Belzowska, 2019/04/28
# Iris Flower Data Analysis

# Investigating the data: Min, Max, Mean, Median and Standard Deviation

import pandas as pd

iris_data = pd.read_csv('irisdata_project_2019.csv')

iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

print('                                                     ')
print('The shape of the data')
print('                                                     ')
print(iris_data.shape)
print('=====================================================')
print('                                                     ')
print('The minimum value of the columns')
print('                                                     ')
print(iris_data.min())
print('=====================================================')
print('                                                     ')
print('The maximum value of the columns')
print('                                                     ')
print(iris_data.max())
print('=====================================================')
print('                                                     ')
print('The mean value of the columns')
print('                                                     ')
print(iris_data.mean())
print('=====================================================')
print('                                                     ')
print('The median value of the columns')
print('                                                     ')
print(iris_data.median())
print('=====================================================')
print('                                                     ')
print('The standard deviation value of the columns')
print('                                                     ')
print(iris_data.std())
print('=====================================================')
