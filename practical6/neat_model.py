
# import the libraries

import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import datetime

# define pythagorean distance calculator

distances = []

def distance_between(m,n):
    distance_squared = (agents[m].x-agents[n].x)**2 + (agents[m].y-agents[n].y)**2
    distance = distance_squared**(1/2)
    distances.append(distance)
    return distance

# set variables

num_of_agents = int(eval(input("How many agents shall we have?\n")))
print("Okay, " + str(num_of_agents) + " agents.")
num_of_iterations = int(eval(input("And how many steps shall they each take?\n")))
print("Right, " + str(num_of_iterations) + " iterations. Here we go!")
agents = []

# read environment data

environment = []

dataset = open('in.txt', newline='')
reader = csv.reader(dataset)
for row in reader:
    rowlist = []
    for numeric_string in row:
        value = int(numeric_string)
        rowlist.append(value)
    environment.append(rowlist)
dataset.close() 

# make the agents, passing in environment

for i in range(num_of_agents):
    agents.append(agentframework.Agent(env = environment))


# move the agents

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()


# measure distance between the agents

for i in range(num_of_agents - 1):
    for j in range (i + 1, num_of_agents):
        distance_between(i,j)

# find the maximum and minimum distances between your agents

print("Max Distance between two agents is " + str(max(distances)))
print("Min Distance between two agents is " + str(min(distances)))

# plot the agents

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# write out environment as a file at the end

## create unique data stamp for filename

now=str(datetime.datetime.now())

unique=''

for char in now:

    if char in '0123456789':
        unique += char


env_file = open('env_files\\' + unique + 'env_file.csv', 'w')
for row in environment:
    for value in row:
        env_file.write(str(value)+',')
    env_file.write('\n')

# a second file that writes out the total amount stored by all the agents on a line

store_file = open('store_file.txt', 'a')

store_file.write('\n\n' + unique + '\n')

for i in range(num_of_agents):
    store_file.write(str(agents[i]) + ',')