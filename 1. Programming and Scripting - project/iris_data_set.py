# Karolina Szafran-Belzowska, 2019/04/15
# Iris flower Data analysis

# This code will print the whole Fisher's iris flower data

import csv
with open('irisdata.csv') as data:
    readCSV = csv.reader(data, delimiter=',')
    
    for columns in readCSV:
        print(columns)



