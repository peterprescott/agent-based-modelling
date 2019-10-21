# Import standard libraries.

from sys import argv
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation


from model import create_env, create_agents, save_data

fig = matplotlib.pyplot.figure(figsize=(7, 7))

def run_gui():
    def run():
        animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
        canvas.draw()
    
    animated = 'ANIMATED'
    root = tkinter.Tk()
    root.wm_title("Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    menu_bar = tkinter.Menu(root)
    root.config(menu=menu_bar)
    model_menu = tkinter.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=model_menu)
    model_menu.add_command(label="Run model", command=run)
    tkinter.mainloop()

create_env()
create_agents()
save_data()
run_gui()
