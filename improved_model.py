import random

agents = []

# 

y0 = random.randint(0,99)

x0 = random.randint(0,99)

agents.append([y0,x0])

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

y1 = random.randint(0,99)
x1 = random.randint(0,99)

agents.append([y1,x1])

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