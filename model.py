import random

# Make a y variable.

y0 = 50
#~ # test y0 has been assigned correctly
#~ print("y0 = "+str(y0))


# Make a x variable.

x0 = 50
#~ # test x0 has been assigned correctly
#~ print("x0 = "+str(x0))

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
# Work out the distance between the two sets of y and xs.