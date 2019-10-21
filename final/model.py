#~ model.py


# Import any necessary libraries.

from sys import argv
import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import csv
import datetime
import time
import os
import platform

# Import home-made modules.

import agentframework
import read_cmd
import web_scraper


# Define independent pieces of our procedure as functions.

def create_env(file):
    """Creates an environment from a CSV file."""
    
    environment = []

    with open(file, newline='') as dataset:
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
    
    return environment

    
def create_agents(environment):
    """Make the agents, passing in environment."""

    agents = []

    for i in range(num_of_agents):
        j = i % len(y_values)

        ## multiply values by 3 to spread across entire environment
        y = 3*y_values[j]
        x = 3*x_values[j]

        agents.append(agentframework.Agent(environment, agents, y, x))
    
    return agents


def update(frame_number):
    """Updates the visualization."""
    
    fig.clear()   
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=max(max(environment)))
    matplotlib.pyplot.xlim(0, agents[0].env_width)
    matplotlib.pyplot.ylim(0, agents[0].env_height)

    random.shuffle(agents)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
    
    for agent in agents:
        matplotlib.pyplot.scatter(agent.y,agent.x, c="#ffffff")


def show_plot():
    """
    Shows animated plot of Agents' movements.
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    matplotlib.pyplot.show()


def save_data():
    """"
    Write environment to CSV file,
    and Agent data to text file.
    """

    ## create unique data stamp for filename
    unique = ''
    now = str(datetime.datetime.now())
    for char in now:
        if char in '0123456789':
            unique += char

    env_file = open(os.path.join('output_files','env_files',f'{unique}env_file.csv'), 'w')
    for row in environment:
        for value in row:
            env_file.write(str(value)+',')
        env_file.write('\n')

    with open(os.path.join('output_files','store_file.txt'), 'a') as store_file:
        store_file.write('\n\n' + unique + '\n')
        
        for i in range(num_of_agents):
            store_file.write(str(agents[i]) + ',')


# Now run our model.

## Time it.
start = time.perf_counter()

## Read parameters from command line (if none set, then defaults).
num_of_agents, neighbourhood, num_of_iterations, animate = read_cmd.parameters(argv)

## Scrape x- and y-values from web.
url = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
y_values, x_values = web_scraper.scrape(url)

## Create environment from CSV file.
environment = create_env(os.path.join('output_files','env_files','20191021122948049878env_file.csv'))

## Create agents.
agents = create_agents(environment)

## Only show animated plot if script is being run directly, rather than being imported. 

if animate == "ANIMATE":
    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    show_plot()

## Save data.
save_data()

## Finish timing.
end = time.perf_counter()
time_result = str(end - start)
tech = platform.uname()

with open(os.path.join('output_files','time_file.csv'), 'a') as time_file:
    time_file.write('\n\n' + animate +  ',' +
							str(num_of_agents) + ',' +
                            str(neighbourhood) + ',' +
                            str(num_of_iterations) + ',' +
                            str(time_result) + ',' +
                            tech.system + str(tech.release) + ',' +
                            tech.machine)
