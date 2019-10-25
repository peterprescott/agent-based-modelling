# Agent-Based Modelling in Python
A project done as part of [the Data CDT](https://datacdt.org/)'s GEOG5995M/ENVS802 module: **Programming For Social Scientists**.

Contents:
[Intro](#intro)
[Installation](#install)
[Discussion](#discuss)

<a name="intro"></a>
## Intro
This project is the result of working through [the practical exercises](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/) put together by [Dr. Andy Evans](https://ajevans.github.io/) to teach core programming skills to students starting a four-year integrated PhD and MSc in Data Analytics and Society.

It is 'licensed' under the [The Unlicense](https://unlicense.org/), and available on [my Github](https://github.com/peterprescott/agent-based-modelling). 

It is intended to be [run from the command line](https://www.howtogeek.com/437682/command-lines-why-do-people-still-bother-with-them/), though the project includes the beginnings of a Tkinter GUI, as well as a proof-of-concept of a web-page GUI with code written in JavaScript instead of Python.

<a name="install"></a>
## Installation
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

If you are interested in testing the speed of the model with iterations of various orders of magnitude, then you can use the ```tests.sh``` or ```tests.bat``` script in the `tests` folder to do so efficiently. 

[![asciicast](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.svg)](https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA)
<script id="asciicast-WO9oNzJcxv3veBcjtm7FRpjEA" src="https://asciinema.org/a/WO9oNzJcxv3veBcjtm7FRpjEA.js" async></script>

But you probably want to be able to **see** what your model is actually doing. We use [Matplotlib](https://matplotlib.org/) for the graphic visualization. You then run ```python run_model.py animate```, or just ```python run_model.py a``` if you're feeling lazy. (In fact, any word beginning with 'a' should do the trick!)

```console
pip install -r graphic_requirements.txt
python run_model.py animate
```

You should then see a visual animation of your model as it runs: specifically, white and black dots wobbling around on a yellowly-green square. The white dots represent male rabbits; the black dots female rabbits. 

[![Visual animation of the model](https://geodemographics.co.uk/images/abm.gif)]

<a name="discuss"></a>
## Discussion
Those practicals developed a class of Agent that took random walks across a two-dimensional Environment, stored resources from that Environment, and interacted with other Agents within a certain specified 'neighbourhood' range.

I then extended the model by writing a child Rabbit class that inherited move() and eat() functions from the parent Agent class, but added the idea of ageing, death, and reproduction.

Those practicals developed a class of Agent that took random walks across a two-dimensional Environment, stored resources from that Environment, and interacted with other Agents within a certain specified 'neighbourhood' range.

I then extended the model by writing a child Rabbit class that inherited move() and eat() functions from the parent Agent class (though now with the idea that eating gives the energy essential for life, and for movement)...

```python

    def move(self):
        """Rabbit moves just like an Agent, but uses energy to do so."""
        
        Agent.move(self)
        
        self.energy -= 5

    def eat(self): 
        """A Rabbit eats just like an Agent, but dies if it runs out of energy."""
        
        if self.energy < 0:
            self.die()
            print(f"{self} died of starvation.")

        Agent.eat(self)

```

and then added a ```mate(range)``` function, as well as get_older() and die() functions.

```python

    def mate(self, range):
        """Mature female rabbits become pregnant whenever male is in range,
        and then give birth after ten steps."""
                
        if self.sex == "female" and self.age > 10:

            if self.pregnant > 0:
                self.energy -= 5
                self.pregnant += 1
                if self.pregnant == 10:
					### create new baby rabbit
                    self.agents.append(Rabbit(self.environment, self.agents, self.x, self.y, self.lifespan))
                    print(f'{self.name} gave birth.')
                    self.pregnant = 0
            else:
                for agent in self.agents:
                    if self.distance_between(agent) <= range:
                        if agent.sex == "male":
                            self.pregnant = 1
```
