#~ agentframework.py

import csv
import os
import sys
import random
import names


class Environment:
    """
    Transforms a CSV file into a 2-d environment with which an agent can interact.
    
    Attributes:
        env: A list of equal-length lists of integers representing grass in a field.
    """
    
    def __init__(self, file):
        """Initialize Environment from a given CSV file.
        
        Args:
            file: A CSV file of integers representing grass in a field."""
        
        environment = []

        with open(os.path.join(sys.path[0], file), newline='') as dataset:
            reader = csv.reader(dataset)
            for row in reader:
                rowlist = []
                for numeric_string in row:
                    try:
                        value = int(numeric_string)
                        rowlist.append(value)
                    except:
                        # When loading an environment saved by save_env(),
                        # python is tricked by the comma at the end of each line
                        # into trying to convert the empty string '' to an int.
                        # This exception stops that from being a problem.
                        pass


                environment.append(rowlist)
                
        self.env = environment



class Agent:
    """An Agent takes a random walk through a two-dimensional environment.
    
    Attributes:
        environment: The environment in which the Agent is moving.
            A list of equal-length lists of integers.
        env_height: The height of the environment.
        env_width: The width of the environment.
        y: Integer. The Agent's y-coordinate within the environment.
        x: Integer. The Agent's x-coordinate within the environment.
        
    """
    
    def __init__(self, env, agents, x, y):
        """Initialize Agent.
        
        Args:
            env: The environment in which the Agent is moving.
                 A list of equal-length lists of integers.
            agents: The list of other Agents with which the Agent is interacting.
            x: The Agent's initial x-coordinate within the environment.
            y: The Agent's initial y-coordinate within the environment.
        """

        self.environment = env
        self.env_height = len(env)
        self.env_width = len(env[0])

        self.y = y
        self.x = x
        self.step_size = 1

        self.energy = 30

        self.agents = agents
        
        self.colour = "white"

    def move(self):
        """Move agent with random unit-sized step in each of two dimensions."""
        
        if random.random() < 0.5:
            self.y = (self.y + self.step_size) % self.env_height
        else:
            self.y = (self.y - self.step_size) % self.env_height

        if random.random() < 0.5:
            self.x = (self.x + self.step_size) % self.env_width
        else:
            self.x = (self.x - self.step_size) % self.env_width

        return [self.y, self.x]

    def eat(self): 
        """Define an agent's eating of resource from environment."""

        if self.environment[self.x][self.y] > 10:
            self.environment[self.x][self.y] -= 10
            self.energy += 10

        if self.environment[self.x][self.y] <= 10:
            self.energy += (self.environment[self.x][self.y])
            self.environment[self.x][self.y] = 0
            
    def distance_between(self,agent):
        """Find Euclidean distance between this Agent and another Agent.
        
        Args:
            agent: Another Agent.
        """
        
        distance_squared = (self.x-agent.x)**2 + (self.y-agent.y)**2
        distance = distance_squared**(1/2)
        return distance


#Now let's extend the model.
class Rabbit(Agent):
    """A Rabbit is an Agent that eats grass, reproduces, ages, and dies."""
    
    def __init__(self, env, agents, x, y, lifespan):
        """Initialize Rabbit.
        
        Args:
            env: The environment in which the Agent is moving.
                 A list of equal-length lists of integers.
            agents: The list of other Agents with which the Agent is interacting.
            x: Integer. The Agent's initial x-coordinate within the environment.
            y: Integer. The Agent's initial y-coordinate within the environment.
            lifespan: Integer value at which a Rabbit dies of old age.
        """
        
        Agent.__init__(self, env, agents, x, y)
        
        self.age = 0
        self.lifespan = lifespan
        
        self.sex = random.choice(["male", "female"])
        if self.sex == "female":
            self.pregnant = 0
            self.colour = "k ie. black"

        self.name = names.get_first_name(gender=self.sex)
    
    def __repr__(self):
        """A Rabbit is known simply by its first name."""
        return self.name

    def move(self):
        """Rabbit moves just like an Agent, but uses energy to do so."""
        
        Agent.move(self)
        
        self.energy -= 5
    
    def eat(self): 
        """A Rabbit eats just like an Agent, but dies if it runs out of energy."""
        
        if self.energy < 0:
            self.die()
            # ~ print(f"{self} died of starvation.")

        Agent.eat(self)
            
    def mate(self, range):
        """Mature female rabbits become pregnant whenever male is in range,
        and then give birth after ten steps.
        
        Args:
            range: Integer. Distance within which Rabbits mate.
        """
                
        if self.sex == "female" and self.age > 10:

            if self.pregnant > 0:
                self.energy -= 5
                self.pregnant += 1
                if self.pregnant == 10:
                    ### create new baby rabbit
                    self.agents.append(Rabbit(self.environment, self.agents, self.x, self.y, self.lifespan))
                    # ~ print(f'{self.name} gave birth.')
                    self.pregnant = 0
            else:
                for agent in self.agents:
                    if self.distance_between(agent) <= range:
                        if agent.sex == "male":
                            self.pregnant = 1

    def get_older(self):
        """Rabbits age; and when their age exceeds their lifespan, they die."""
        
        self.age += 1
        if self.age > self.lifespan:
            self.die()
            # ~ print(f"{self} died of old age.")

    def die(self):
        """When a Rabbit dies, it is removed from the list of living Rabbits."""

        try:
            index = self.agents.index(self)
            self.agents.pop(index)
        except ValueError:
            # I haven't worked out why, but sometimes this thows errors.
            # ~ print('Something went wrong, but we will press on')
            pass

# If you have the time...
class Fox(Agent):
    """TODO: A Fox is an Agent that hunts rabbits and eats them."""
    
       
    pass
