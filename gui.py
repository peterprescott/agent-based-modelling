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
from run_model import create_rabbits, rabbits_interact, save_data
from agentframework import Environment
        
def update(frame_number):
    """Updates the visualization for matplotlib."""

    fig.clear()
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=max(max(environment)))
    matplotlib.pyplot.xlim(0, rabbits[0].env_width)
    matplotlib.pyplot.ylim(0, rabbits[0].env_height)

    rabbits_interact(rabbits, neighbourhood)

    for agent in rabbits:
        matplotlib.pyplot.scatter(agent.y, agent.x, c=agent.colour[0])

def run():
    """Runs the Graphical User Interface."""
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.draw()

# Only run if script is called directly.
if __name__ == '__main__':
    ## Read parameters from command line
    ## (if none set, will set defaults as defined in read_cmd.py).
    parameters = read_cmd.parameters(argv)
    num_of_rabbits, lifespan, neighbourhood, num_of_iterations, animate = parameters

    ## Scrape initial x- and y-values from webpage.
    url = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
    scraped_coordinates = web_scraper.scrape(url)

    ## Create environment from CSV file.
    environment = Environment("in.txt").env

    ## Create rabbits.
    rabbits = create_rabbits(environment, num_of_rabbits, scraped_coordinates, lifespan)


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
