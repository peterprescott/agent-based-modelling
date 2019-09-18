import random

# define Agent class

class Agent:

    '''An Agent that takes a random walk through two-dimensions'''
    
    def __init__(self, env, agents):

        self.environment = env
        self.env_height = len(env)
        self.env_width = len(env[0])

        self._y = random.randint(0, self.env_height-1)
        self._x = random.randint(0, self.env_width-1)

        self.store = 0

        self.agents = agents

        return

    ## do the decent object oriented thing: https://docs.python.org/3/library/functions.html#property

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def del_y(self):
        del self._y

    y = property(get_y, set_y, del_y, "I'm the 'y' property.")


    ## define representation, so that when you print an agent you see something intelligible.

    def __repr__(self):

        return "{'store':'" + str(self.store) + "','y':'" + str(self.y) + "','x':'" + str(self.x) + "'}"

    ## define an agent's move, ie. a random unit-sized step in each of two dimensions

    def move(self):

        if random.random() < 0.5:
            self.y = (self.y + 1) % self.env_height
        else:
            self.y = (self.y - 1) % self.env_height

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.env_width
        else:
            self.x = (self.x - 1) % self.env_width

        return [self.y, self.x]

    ## define an agent's eating of resource from environment

    def eat(self): # can you make it eat what is left?

        if self.environment[self.y][self.x] > 10:

            self.environment[self.y][self.x] -= 10

            self.store += 10

        if self.environment[self.y][self.x] <= 10:

            self.store += self.environment[self.y][self.x]

            self.environment[self.y][self.x]

        if self.store > 100:

            self.environment[self.y][self.x] += self.store

            self.store = 0

        return

    ## define pythagorean distance calculator

    def distance_between(self,agent):
        distance_squared = (self.x-agent.x)**2 + (self.y-agent.y)**2
        distance = distance_squared**(1/2)
        return distance

    ## define an agent's sharing of 'eaten' resource with neighbour agents within neighbourhood proximity range

    def share_with_neighbours(self, neighbourhood):

        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                self.store = agent.store = (self.store + agent.store)/2

        return
