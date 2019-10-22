# Import standard libraries.

from sys import argv
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation

import read_cmd
import web_scraper
from model import create_env, create_agents, agents_interact, save_data

def update(frame_number):
    """Updates the visualization."""

    fig.clear()
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=max(max(environment)))
    matplotlib.pyplot.xlim(0, agents[0].env_width)
    matplotlib.pyplot.ylim(0, agents[0].env_height)

    agents_interact(agents, neighbourhood)

    for agent in agents:
        matplotlib.pyplot.scatter(agent.y, agent.x, c="#ffffff")

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.draw()


## Read parameters from command line
## (if none set, will set defaults as defined in read_cmd.py).
parameters = read_cmd.parameters(argv)
num_of_agents, neighbourhood, num_of_iterations, animate = parameters

## Scrape initial x- and y-values from webpage.
url = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
scraped_coordinates = web_scraper.scrape(url)

## Create environment from CSV file.
environment = create_env("in.txt")

## Create agents.
agents = create_agents(environment, num_of_agents, scraped_coordinates)


# Configure Tkinter.
root = tkinter.Tk()
root.wm_title("Model")
fig = matplotlib.pyplot.figure(figsize=(7, 7))
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


tkinter.mainloop()
