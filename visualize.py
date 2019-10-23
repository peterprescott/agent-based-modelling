import os
import imageio
import matplotlib
import matplotlib.pyplot
import matplotlib.animation

from run_model import agents_interact

def show_plot(environment, agents, neighbourhood, num_of_iterations):
    """Shows animated plot of Agents' movements."""

    fig = matplotlib.pyplot.figure(figsize=(7, 7))

    def update(frame_number):
        """Updates the visualization."""

        fig.clear()
        matplotlib.pyplot.imshow(environment, vmin=0, vmax=500)
        matplotlib.pyplot.xlim(0, agents[0].env_width)
        matplotlib.pyplot.ylim(0, agents[0].env_height)

        agents_interact(agents, neighbourhood)

        for agent in agents:
            matplotlib.pyplot.scatter(agent.y, agent.x, c=agent.tribe[0])
        
        matplotlib.pyplot.savefig(os.path.join('output_files','gif',f"{frame_number}.jpg"), quality=10)

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    matplotlib.pyplot.show()

    with imageio.get_writer(os.path.join('output_files','gif','saved_animation.gif'), mode="I",
                            duration=0.5) as writer:
        for file in range(num_of_iterations):
            image = imageio.imread(os.path.join('output_files','gif',f"{file}.jpg"))
            writer.append_data(image)
            os.remove(os.path.join('output_files','gif',f"{file}.jpg"))

