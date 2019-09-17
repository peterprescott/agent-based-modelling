import random
import operator 
import matplotlib.pyplot

agents = []

num_of_agents = 10

num_of_iterations = 100

# add full number of agents in one smooth move

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

# plot arena

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)


# move agents

## for each iteration
for i in range(num_of_iterations):
    ##
    for k in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[k][1],agents[k][0])

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

        agents[j][0] = agents[j][0] % 100
        agents[j][1] = agents[j][1] % 100


# Make agent furthest east, ie. greatest x-value, a different colour
# max(agents, key=operator.itemgetter(1))

furthest_east = max(agents, key=operator.itemgetter(1))
print(furthest_east)

matplotlib.pyplot.scatter(furthest_east[1], furthest_east[0], color='red')

matplotlib.pyplot.show()