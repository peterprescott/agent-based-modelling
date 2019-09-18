
# import the libraries

from sys import argv
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import csv
import datetime

# time it!

import time

start = time.perf_counter()


# import the agentframework

import agentframework

# set variables

while True:
    try:
        script, plot, num_of_agents, num_of_iterations, neighbourhood = argv
        break
    except ValueError:
        print('Oops, you forgot to define parameters from command line...\nFear not--we will just set the defaults.')
        # set defaults
        plot = 0
        num_of_agents = 5
        num_of_iterations = 100
        neighbourhood = 10
        break

type(num_of_agents)

while True:
    try:
        num_of_agents = int(num_of_agents)
        break
    except ValueError:
        print("Oops! You didn't give a valid input for num_of_agents. So we'll default to 10.")
        num_of_agents = 10
        
print("Okay, " + str(num_of_agents) + " agents.")

while True:
    try:
        num_of_iterations = int(num_of_iterations)
        break
    except ValueError:
        print("Oops! You didn't give a valid input for num_of_iterations. So we'll default to 10.")
        num_of_iterations = 10    
print("Right, " + str(num_of_iterations) + " iterations.")

while True:
    try:
        neighbourhood = int(neighbourhood)
        break
    except ValueError:
        print("Oops! You didn't give a valid input for neighbourhood. So we'll default to 10.")
        neighbourhood = 10
print(f"Neighbourhood size: {neighbourhood}. Okay, let's go!")

agents = []


# read environment data

environment = []

dataset = open('in.txt', newline='')
reader = csv.reader(dataset)
for row in reader:
    rowlist = []
    for numeric_string in row:
        value = int(numeric_string)
        rowlist.append(value)
    environment.append(rowlist)
dataset.close() 

# make the agents, passing in environment

for i in range(num_of_agents):
    agents.append(agentframework.Agent(env = environment, agents = agents))

# define update to move the agents
      
def update(frame_number):
    
    fig.clear()   

    random.shuffle(agents)

    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
        
   
    
    for agent in agents:
        matplotlib.pyplot.scatter(agent.y,agent.x)


# stop the timer

end = time.perf_counter()

time_result = "time = " + str(end - start)


# plot the agents (unless argv withholds permission)

if plot != "0":

    fig = matplotlib.pyplot.figure(figsize=(7, 7))

    # ~ matplotlib.pyplot.xlim(0, agents[0].env_width)
    # ~ matplotlib.pyplot.ylim(0, agents[0].env_height)
    # ~ fig = matplotlib.pyplot.imshow(environment)

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

    matplotlib.pyplot.show()




# write out environment as a file at the end

    ## create unique data stamp for filename

now = str(datetime.datetime.now())

unique = ''

for char in now:

    if char in '0123456789':
        unique += char


env_file = open('env_files\\' + unique + 'env_file.csv', 'w')
for row in environment:
    for value in row:
        env_file.write(str(value)+',')
    env_file.write('\n')

# a second file that writes out the total amount stored by all the agents on a line

store_file = open('store_file.txt', 'a')
store_file.write('\n\n' + unique + '\n')

time_file = open('time_file.txt', 'a')
time_file.write(f'\n\n num_of_agents = {num_of_agents}, num_of_iterations = {num_of_iterations}, neighbourhood = {neighbourhood}\n {time_result}')

for i in range(num_of_agents):
    store_file.write(str(agents[i]) + ',')

