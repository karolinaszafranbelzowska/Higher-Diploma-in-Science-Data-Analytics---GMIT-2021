# Karolina Szafran-Belzowska, 2019/04/15
# Iris flower data analysis

# first column (sepal length)

import csv
with open('irisdata_project_2019.csv') as data:
    readCSV = csv.reader(data, delimiter=',')
    
    for row in readCSV:
        print(row[0])


