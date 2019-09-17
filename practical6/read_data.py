import matplotlib.pyplot
import csv

## https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/part7/index.html
environment = []
rowlist = []

dataset = open('in.txt', newline='')
reader = csv.reader(dataset)
for row in reader:
    rowlist = []
    for numeric_string in row:
        value = int(numeric_string)
        rowlist.append(value)
    environment.append(rowlist)
dataset.close() 

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()