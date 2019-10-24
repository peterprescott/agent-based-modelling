import os
import imageio
import matplotlib
import matplotlib.pyplot
import matplotlib.animation

from run_model import agents_interact

save_gif = "no"

def show_plot(environment, agents, neighbourhood, num_of_iterations):
    """Shows animated plot of Agents' movements."""

    fig = matplotlib.pyplot.figure(figsize=(7, 7))

    def update(frame_number):
        """Updates the visualization."""

        fig.clear()
        rabbit_count = len(agents)
        if rabbit_count > 0:
            txt = f"[{frame_number}] There are {rabbit_count} rabbits."
        else:
            txt = "There are no more rabbits."
        fig.text(.05,.05,txt)
        matplotlib.pyplot.imshow(environment, vmin=0, vmax=250)
        matplotlib.pyplot.xlim(0, agents[0].env_width)
        matplotlib.pyplot.ylim(0, agents[0].env_height)

        agents_interact(agents, neighbourhood)

        for agent in agents:
            matplotlib.pyplot.scatter(agent.y, agent.x, c=agent.colour[0])
        
        if save_gif == "YES":
            matplotlib.pyplot.savefig(os.path.join('output_files','gif',f"{frame_number}.jpg"), quality=50)

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    matplotlib.pyplot.show()

    if save_gif == "YES":
        with imageio.get_writer(os.path.join('output_files','gif','saved_animation.gif'), mode="I",
                                duration=0.5) as writer:
            for file in range(num_of_iterations):
                image = imageio.imread(os.path.join('output_files','gif',f"{file}.jpg"))
                writer.append_data(image)
                os.remove(os.path.join('output_files','gif',f"{file}.jpg"))

