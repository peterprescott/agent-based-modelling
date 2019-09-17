import matplotlib.pyplot

## https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/part7/index.html
dataset = open("in.txt")


f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)

f.close()


matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()