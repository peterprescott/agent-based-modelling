import random

class Agent:

    '''An Agent that takes a random walk through two-dimensions'''
    
    def __init__(self, env, y = random.randint(0,99), x = random.randint(0,99)):

        self._y = y
        self._x = x

        self.environment = env
        self.store = 0

        return

# do the decent object oriented thing: https://docs.python.org/3/library/functions.html#property

    def get_x(self):
        return self._x

    def set_x(self, value = random.randint(0,99)):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

    def get_y(self):
        return self._y

    def set_y(self, value = random.randint(0,99)):
        self._y = value

    def del_y(self):
        del self._y

    y = property(get_y, set_y, del_y, "I'm the 'y' property.")



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

