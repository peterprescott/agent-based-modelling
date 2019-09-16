import random
import operator 
import matplotlib.pyplot

agents = []

num_of_agents = 10

# add full number of agents in one smooth move

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])


# Change y and x based on random numbers.

y0_direction = random.random()

if y0_direction < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

x0_direction = random.random()

if x0_direction < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

print(agents[0])


# Make a second set of y and xs, and make these change randomly as well.


y1_direction = random.random()
x1_direction = random.random()

if y1_direction < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if x1_direction < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
print (agents[1])


# Work out the distance between the two sets of y and xs.

# Pythagoras: x**2 + y**2 = z**2

distance_squared = (agents[1][1]-agents[0][1])**2 + (agents[0][1]-agents[0][0])**2

distance = distance_squared**(1/2)

print(distance)

# Print Agent with greatest y-value
print(max(agents, key=operator.itemgetter(0)))

# Print Agent with greatest x-value
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# Make agent furthest east, ie. greatest x-value, a different colour
# max(agents, key=operator.itemgetter(1))

furthest_east = max(agents, key=operator.itemgetter(1))
print(furthest_east)

matplotlib.pyplot.scatter(furthest_east[1], furthest_east[0], color='red')

matplotlib.pyplot.show()