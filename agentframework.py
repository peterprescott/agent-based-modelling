import random

class Agent:

    '''An Agent that takes a random walk through two-dimensions'''
    
    def __init__(self, y = random.randint(0,99), x = random.randint(0,99)):

        self.y = y
        self.x = x

        return

    def __repr__(self):

        return "[" + str(self.y) + ", " + str(self.x) + "]"

    def move(self):

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        return [self.y, self.x]

test = Agent(50,50)

for i in range(0, 100):
    test.move()

print(test)