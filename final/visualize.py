import matplotlib
import matplotlib.pyplot
import matplotlib.animation

from model import agents_interact

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
            matplotlib.pyplot.scatter(agent.y, agent.x, c=agent.tribe[0])

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    matplotlib.pyplot.show()

def visualize(environment, agents, neighbourhood, num_of_iterations):
        fig = matplotlib.pyplot.figure(figsize=(7, 7))
        show_plot(fig, environment, agents, neighbourhood, num_of_iterations)
