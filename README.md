# Agent-Based Modelling in Python
A project done as part of [the Data CDT](https://datacdt.org/)'s GEOG5995M/ENVS802 module: **Programming For Social Scientists**.

This project is the result of working through [the practical exercises](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/) put together by [Andy Evans](https://ajevans.github.io/) to teach core programming skills to students starting a four-year integrated PhD and MSc in Data Analytics and Society.

It is 'licensed' under the [The Unlicense](https://unlicense.org/), and available on [my Github](https://github.com/peterprescott/agent-based-modelling). 

It is intended to be [run from the command line](https://www.howtogeek.com/437682/command-lines-why-do-people-still-bother-with-them/), though the project includes the beginnings of a Tkinter GUI, as well as a proof-of-concept of a web-page GUI with code written in JavaScript instead of Python.

You need to have Git and Python installed. If you don't, use your system's recommended package manager to download them from the command line. (For Windows, use [Chocolatey](https://chocolatey.org/install).)

(*Note: [Python 3.8](https://docs.python.org/3/whatsnew/3.8.html) was released on October 14th, 2019, and at time of writing [is not supported by Matplotlib](https://stackoverflow.com/questions/58386191/python-pip-failed-installing-matplotlib), so you need to [install Python 3.7 specifically](https://chocolatey.org/packages/python/3.7.2), otherwise you will get Python 3.8 and your installation of Matplotlib will fail.*)

Then clone the Github repository, and navigate into the project folder. You can then immediately run the model:

```console
python --version
git --version
git clone https://github.com/peterprescott/agent-based-modelling
cd agent-based-modelling
pip install -r requirements.txt
python run_model.py
```

[![asciicast](https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2.svg)](https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2)
<script id="asciicast-6ldhFPdvzJSHvyrVz0bcSQJp2" src="https://asciinema.org/a/6ldhFPdvzJSHvyrVz0bcSQJp2.js" async></script>

If everything is working correctly, you should be told the *Initial Parameters* with which the model is running (as ```python run_model.py``` doesn't specify any, the model will use the defaults), and that the various steps of running the model have successfully taken place, including how long it took to run the model, and the details of the machine you are using to run it. The output data is saved in the ```output_files``` folder.

If you are interested in testing the speed of the model with iterations of various orders of magnitude, then you can use the ```tests.sh``` or ```tests.bat``` script to do so efficiently. 

[![asciicast](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.svg)](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA)
<script id="asciicast-WO9oNzJcxv3veBcjtm7FRpjEA" src="https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.js" async></script>

But you probably want to be able to **see** what your model is actually doing. We use [Matplotlib](https://matplotlib.org/) for the graphic visualization. You then run ```python run_model.py animate```, or just ```python run_model.py a``` if you're feeling lazy. (In fact, any word beginning with 'a' should do the trick!)

```console
pip install -r graphic_requirements.txt
python run_model.py animate
```

You should then see a visual animation of your model as it runs: specifically, white and black dots wobbling around on a yellowly-green square. The white dots represent male rabbits; the black dots female rabbits. 

[![Visual animation of the model](https://geodemographics.co.uk/images/abm.gif)]

We've extended the generic agent-based model developed in the practicals into a model of multiplying rabbit populations.

```python
class Rabbit(Agent):
    """A Rabbit is an Agent that eats grass, reproduces, ages, and dies."""
    
    def __init__(self, env, agents, x, y, lifespan):
        """Initialize Rabbit"""
        
        Agent.__init__(self, env, agents, x, y)
        
        self.age = 0
        self.lifespan = lifespan
        
        self.sex = random.choice(["male", "female"])
        self.name = names.get_first_name(gender=self.sex)
        
        if self.sex == "female":
            self.pregnant = 0
            self.colour = "k ie. black"
    
    def __repr__(self):
        return self.name

    def move(self):
        """Rabbit moves just like an Agent, but uses energy to do so."""
        
        Agent.move(self)
        
        self.energy -= 5
    
    def eat(self): 
        """Define an agent's eating of resource from environment."""
        
        if self.energy < 0:
            self.die()
            print(f"{self} died of starvation.")

        if self.environment[self.x][self.y] > 20:
            # Rabbits digest inefficiently: 
            # they only get 1 unit of energy from 2 units of grass
            self.environment[self.x][self.y] -= 20
            self.energy += 10

        if self.environment[self.x][self.y] <= 20:
            self.energy += (self.environment[self.x][self.y])/2
            self.environment[self.x][self.y] = 0
            
    def mate(self, range):
        """Mature female rabbits become pregnant whenever male is in range,
        and then give birth after ten steps."""
                
        if self.sex == "female" and self.age > 10:

            if self.pregnant > 0:
                self.energy -= 5
                self.pregnant += 1
                if self.pregnant == 10:
                    self.agents.append(Rabbit(self.environment, self.agents, self.x, self.y, self.lifespan))
                    print(f'{self.name} gave birth.')
                    self.pregnant = 0
            else:
                for agent in self.agents:
                    if self.distance_between(agent) <= range:
                        if agent.sex == "male":
                            self.pregnant = 1

    def get_older(self):
        """Rabbits age."""
        
        self.age += 1
        if self.age > self.lifespan:
            self.die()
            print(f"{self} died of old age.")

    def die(self):
        """Rabbits die."""

        try:
            index = self.agents.index(self)
            self.agents.pop(index)
        except ValueError:
            # I haven't worked out why, but sometimes this thows errors.
            print('Something went wrong, but we will press on')

```
