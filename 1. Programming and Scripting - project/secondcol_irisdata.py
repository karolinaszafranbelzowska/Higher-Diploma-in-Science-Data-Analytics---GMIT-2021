# Karolina Szafran-Belzowska, 2019/04/25
# Iris flower data analysis

# second column (sepal width)

import csv
with open('irisdata_project_2019.csv') as data:
    readCSV = csv.reader(data, delimiter=',')
    
    for row in readCSV:
        print(row[1])
