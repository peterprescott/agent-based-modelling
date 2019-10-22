#~ model.py

# Import any necessary libraries.

from sys import argv
import random
import csv
import datetime
import time
import os
import platform
import matplotlib
import matplotlib.pyplot
import matplotlib.animation

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


def create_agents(environment, num_of_agents, coordinates):
    """Make the agents, passing in environment, num_of_agents, and initial coordinates."""

    agents = []

    for i in range(num_of_agents):
        if i < len(coordinates):
            x = coordinates[i]["x"]
            y = coordinates[i]["y"]
        else:
            x = random.randint(0, len(environment))
            y = random.randint(0, len(environment[0]))

        agents.append(agentframework.Agent(environment, agents, x, y))

    return agents


def agents_interact(agents, neighbourhood):
    """Shuffle the agents and then make them interact."""

    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)



def show_plot(fig, environment, agents, neighbourhood, num_of_iterations):
    """
    Shows animated plot of Agents' movements.
    """
    def update(frame_number):
        """Updates the visualization."""

        fig.clear()
        matplotlib.pyplot.imshow(environment, vmin=0, vmax=max(max(environment)))
        matplotlib.pyplot.xlim(0, agents[0].env_width)
        matplotlib.pyplot.ylim(0, agents[0].env_height)

        agents_interact(agents, neighbourhood)

        for agent in agents:
            matplotlib.pyplot.scatter(agent.y, agent.x, c="#ffffff")

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    matplotlib.pyplot.show()


def save_data(environment, agents):
    """"
    Write environment to CSV file,
    and Agent data to text file,
    and test data to CSV file.
    """

    ## Create unique data stamp for filename.
    unique = ''
    now = str(datetime.datetime.now())
    for char in now:
        if char in '0123456789':
            unique += char

    ## Save Environment Data.
    env_file = open(os.path.join('output_files', 'env_files', f'{unique}env_file.csv'), 'w')
    for row in environment:
        for value in row:
            env_file.write(str(value)+',')
            ## This method leaves a trailing comma at the end of each line
            ## which could potentially cause problems,
            ## as Python would read such a file and expect an extra value
            ## at the end of each line.
            ## But for the moment we have solved it in create_env()
            ## with an exception when the env_file is loaded.
        env_file.write('\n')

    ## Save Agent Data.
    with open(os.path.join('output_files', 'store_file.txt'), 'a') as store_file:
        store_file.write('\n\n' + unique + '\n')

        for i in range(len(agents)):
            store_file.write(str(agents[i]) + ',')




def my_timer(process):
    """Time the process."""
    def wrapper():
        ## Start timing.
        start = time.perf_counter()

        process()

        ## Finish timing.
        end = time.perf_counter()
        time_result = str(end - start)

        return time_result

    return wrapper



@my_timer
def run_model():
    """Run the model."""
    ## Only show animated plot if explicitly requested --
    ## but assume any word beginning with 'a' is a request to 'animate'.
    if animate.lower()[0] == "a":
        fig = matplotlib.pyplot.figure(figsize=(7, 7))
        show_plot(fig, environment, agents, neighbourhood, num_of_iterations)
    else:
        for i in range(num_of_iterations):
            agents_interact(agents, neighbourhood)

# Only run if script is called directly.
if __name__ == '__main__':

    ## Read parameters from command line
    ## (if none set, will set defaults as defined in read_cmd.py).
    parameters = read_cmd.parameters(argv)
    num_of_agents, neighbourhood, num_of_iterations, animate = parameters

    ## Scrape initial x- and y-values from webpage.
    URL = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
    scraped_coordinates = web_scraper.scrape(URL)

    ## Create environment from CSV file.
    environment = create_env("in.txt")

    ## Create agents.
    agents = create_agents(environment, num_of_agents, scraped_coordinates)


    ## Save data.
    save_data(environment, agents)

    ## Run model and time it.
    time_result = run_model()

    ## Save Test Data.
    tech = platform.uname()
    with open(os.path.join('output_files', 'time_file.csv'), 'a') as time_file:
        time_file.write('\n\n' + animate +  ','
			+ str(num_of_agents) + ','
			+ str(neighbourhood) + ','
			+ str(num_of_iterations) + ','
			+ str(time_result) + ','
			+ tech.node + ','
			+ tech.system + str(tech.release) + ','
			+ tech.machine + ','
			+ tech.processor.replace(',', '') + 'n')
