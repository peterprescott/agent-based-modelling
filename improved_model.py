import random
import operator 
import matplotlib.pyplot

agents = []

num_of_agents = 10

num_of_iterations = 100

# add full number of agents in one smooth move

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

# move agents

## for each iteration
for i in range(num_of_iterations):

    ## for each agent
    for j in range(num_of_agents):
        y_direction = random.random()
        x_direction = random.random()
        if y_direction < 0.5:
            agents[j][0] += 1
        else:
            agents[j][0] -= 1
        if x_direction < 0.5:
            agents[j][1] += 1
        else:
            agents[j][1] -= 1

matplotlib.pyplot.ylim(-100, 200)
matplotlib.pyplot.xlim(-100, 200)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])


# Make agent furthest east, ie. greatest x-value, a different colour
# max(agents, key=operator.itemgetter(1))

furthest_east = max(agents, key=operator.itemgetter(1))
print(furthest_east)

matplotlib.pyplot.scatter(furthest_east[1], furthest_east[0], color='red')

matplotlib.pyplot.show()