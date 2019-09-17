import random

# Make a y variable.

y0 = random.randint(0,99)

# Make a x variable.

x0 = random.randint(0,99)

# Change y and x based on random numbers.

y0_direction = random.random()

if y0_direction < 0.5:
    y0 += 1
else:
    y0 -= 1

x0_direction = random.random()

if x0_direction < 0.5:
    x0 += 1
else:
    x0 -= 1

print(x0,y0)


# Make a second set of y and xs, and make these change randomly as well.

y1 = random.randint(0,99)
x1 = random.randint(0,99)

y1_direction = random.random()
x1_direction = random.random()

if y1_direction < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if x1_direction < 0.5:
    x1 += 1
else:
    x1 -= 1
    
print (x1, y1)


# Work out the distance between the two sets of y and xs.

# Pythagoras: x**2 + y**2 = z**2

distance_squared = (x1-x0)**2 + (y1-y0)**2

distance = distance_squared**(1/2)

print(distance)