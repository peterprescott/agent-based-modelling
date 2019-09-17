import random

class Agent:

    '''An Agent that takes a random walk through two-dimensions'''
    
    def __init__(self, y=50, x=50):

        self.y = y
        self.x = x

        return

    def __repr__(self):

        return "[" + str(self.y) + ", " + str(self.x) + "]"

    def move(self):

        if random.random() < 0.5:
            self.y += 1
        else:
            self.y -= 1

        if random.random() < 0.5:
            self.x += 1
        else:
            self.x -= 1

        return [self.y, self.x]

test = Agent(50,50)

for i in range(0, 100):
    test.move()

print(test)