#~ agentframework.py

import random

# Set Agent's step size.
step_size = 1

class Agent:
    """Define a class of Agent that takes a random walk through a two-dimensional environment."""
    
    def __init__(self, env, agents, x, y):
        """Initialize Agent."""
        self.environment = env
        self.env_height = len(env)
        self.env_width = len(env[0])

        self._y = y
        self._x = x

        self.store = 0

        self.agents = agents

        return

    ## do the decent object oriented thing: https://docs.python.org/3/library/functions.html#property

    def get_x(self):
        """Get x coordinate of Agent."""
        return self._x

    def set_x(self, value):
        """Set x coordinate of Agent."""
        self._x = value

    def del_x(self):
        """Delete x coordinate of Agent."""
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

    def get_y(self):
        """Get y coordinate of Agent."""
        return self._y

    def set_y(self, value):
        """Set y coordinate of Agent."""
        self._y = value

    def del_y(self):
        """Delete y coordinate of Agent."""
        del self._y

    y = property(get_y, set_y, del_y, "I'm the 'y' property.")


    def __repr__(self):
        """Define representation, so that when you print an agent you see something intelligible."""
        return "{'store':'" + str(self.store) + "','y':'" + str(self.y) + "','x':'" + str(self.x) + "'}"


    def move(self):
        """Move agent with random unit-sized step in each of two dimensions."""
		
        if random.random() < 0.5:
            self.y = (self.y + step_size) % self.env_height
        else:
            self.y = (self.y - step_size) % self.env_height

        if random.random() < 0.5:
            self.x = (self.x + step_size) % self.env_width
        else:
            self.x = (self.x - step_size) % self.env_width

        return [self.y, self.x]


    def eat(self): 
        """Define an agent's eating of resource from environment."""
		
        if self.environment[self.x][self.y] > 10:
            self.environment[self.x][self.y] -= 10
            self.store += 10

        if self.environment[self.x][self.y] <= 10:
            self.store += self.environment[self.x][self.y]
            self.environment[self.x][self.y] = 0

		## If Agent has eaten too much, it vomits.
        if self.store > 100:
            self.environment[self.x][self.y] += self.store
            self.store = 0

        return


    def distance_between(self,agent):
        """Find Euclidean distance between this Agent and another Agent."""
        
        distance_squared = (self.x-agent.x)**2 + (self.y-agent.y)**2
        distance = distance_squared**(1/2)
        return distance


    def share_with_neighbours(self, neighbourhood):
        """Share 'eaten' resource with other Agents within neighbourhood proximity range."""
        
        for agent in self.agents:
            if self.distance_between(agent) <= neighbourhood:
                self.store = agent.store = (self.store + agent.store)/2
        return
