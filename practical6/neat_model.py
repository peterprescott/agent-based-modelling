
# import the libraries

import random
import operator
import matplotlib.pyplot
import agentframework

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

# make the agents

for i in range(num_of_agents):
    agents.append(agentframework.Agent())


# move the agents

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

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
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()