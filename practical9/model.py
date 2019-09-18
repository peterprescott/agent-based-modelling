
# import the libraries

from sys import argv
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import csv
import datetime
import requests
import bs4

# scrape web data

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

soup = bs4.BeautifulSoup(content, 'html.parser')

y_values = soup.find_all(attrs={"class" : "y"})

for i in range(len(y_values)):
    y_values[i] = int(y_values[i].text)

x_values = soup.find_all(attrs={"class" : "x"})

for i in range(len(x_values)):
    x_values[i] = int(x_values[i].text)


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
        num_of_agents = 500
        num_of_iterations = 10000
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
    j = i % len(y_values)

    ## multiply values by 3 to spread across entire environment
    y = 3*y_values[j]
    x = 3*x_values[j]

    agents.append(agentframework.Agent(environment, agents, y, x))
      
def update(frame_number):
    
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


# stop the timer

end = time.perf_counter()

time_result = "time = " + str(end - start)


# define figure and animation run()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
    
    # ~ animation = matplotlib.animation.FuncAnimation(fig, update,interval=1, repeat=False, frames=num_of_iterations)

    # ~ matplotlib.pyplot.show()


# tkinter code


def run():
    
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)



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

tkinter.mainloop()
