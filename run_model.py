#~ run_model.py

# Import any necessary libraries.

import sys
from sys import argv
import random
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

def create_rabbits(environment, num_of_rabbits, coordinates, lifespan):
    """Make the rabbits, passing in environment, num_of_rabbits, and initial coordinates."""

    rabbits = []

    for i in range(num_of_rabbits):
        if i < len(coordinates):
            # multiply by 3 to spread scraped coordinates across full 300 x 300 map
            x = 3 * coordinates[i]["x"]
            y = 3 * coordinates[i]["y"]
        else:
            x = random.randint(0, len(environment))
            y = random.randint(0, len(environment[0]))

        rabbits.append(agentframework.Rabbit(environment, rabbits, x, y, lifespan))

    return rabbits



def rabbits_interact(rabbits, neighbourhood=10):
    """Shuffle the rabbits and then make them interact."""

    if len(rabbits) > 0:
        random.shuffle(rabbits)
        for agent in rabbits:
            agent.move()
            agent.eat()
            agent.mate(neighbourhood)
            agent.get_older()
        



def save_data(environment, rabbits):
    """
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
    env_file = open(os.path.join(sys.path[0], 'output_files', 'env_files', f'{unique}env_file.csv'), 'w')
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
    with open(os.path.join(sys.path[0], 'output_files', 'store_file.txt'), 'a') as store_file:
        store_file.write('\n\n' + unique + '\n')

        for i in range(len(rabbits)):
            store_file.write(str(rabbits[i]) + ',')



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
        import visualize
        visualize.show_plot(environment, rabbits, neighbourhood, num_of_iterations)
        ### We import this as as a separate module only at this point,
        ### so that this script can be run without alteration
        ### on devices that do not support visualization,
        ### eg. running through Termux on my Android.

    else:
        for i in range(num_of_iterations):
            print(f"Iteration: {i}/{num_of_iterations}; Rabbits: {len(rabbits)}")
            if len(rabbits) == 0:
                break
            else:
                rabbits_interact(rabbits, neighbourhood)



# Only run if script is called directly.
if __name__ == '__main__':

    ## Read parameters from command line
    ## (if none set, will set defaults as defined in read_cmd.py).
    parameters = read_cmd.parameters(argv)
    num_of_rabbits, lifespan, neighbourhood, num_of_iterations, animate = parameters
    report = f"""##### Initial Parameters #####
    Number of rabbits: {num_of_rabbits}
    Lifespan: {lifespan}
    Number of Iterations: {num_of_iterations}
    """
    print(report)

    ## Scrape initial x- and y-values from webpage.
    URL = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
    scraped_coordinates = web_scraper.scrape(URL)
    print(f"You have successfuly scraped coordinates from {URL}.")

    ## Create environment from CSV file.
    file = "in.txt"
    environment = agentframework.Environment(file).env
    print(f"Environment successfully created from {file}.")
    
    ## Create rabbits.
    rabbits = create_rabbits(environment, num_of_rabbits, scraped_coordinates, lifespan)
    print(f"You have successfuly created {num_of_rabbits} rabbits.")
    
    ## Run model and time it.
    print("We are now going to run the model.")
    time_result = run_model()
    print(f"That took {time_result} seconds.")

    ## Save data.
    save_data(environment, rabbits)
    print(f"Data has been saved.")

    ## Record Test data.
    tech = platform.uname()
    print(f"Machine Details: {tech}.")
    
    with open(os.path.join(sys.path[0], 'output_files', 'time_file.csv'), 'a') as time_file:
        time_file.write('\n\n' + animate +  ','
            + str(num_of_rabbits) + ','
            + str(neighbourhood) + ','
            + str(lifespan) + ','
            + str(num_of_iterations) + ','
            + str(time_result) + ','
            + tech.node + ','
            + tech.system + str(tech.release) + ','
            + tech.machine + ','
            + tech.processor.replace(',', '') + 'n')
