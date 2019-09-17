import random
import operator
import matplotlib.pyplot
import time

start = time.perf_counter()


num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

distances = []

def distance_between(m,n):
    distance_squared = (agents[m][1]-agents[n][1])**2 + (agents[m][0]-agents[n][0])**2
    distance = distance_squared**(1/2)
    distances.append(distance)
    return distance
    

for i in range(num_of_agents - 1):
    for j in range (i + 1, num_of_agents):
        print(distance_between(i,j))

end = time.perf_counter()

# print time taken for calculations
print("time = " + str(end - start))

# find the maximum and minimum distances between your agents
print(max(distances))
print(min(distances))

# show scatter graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

