import os
import imageio
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation

from run_model import rabbits_interact

save_gif = "YES"

def show_plot(environment, rabbits, neighbourhood, num_of_iterations):
    """Shows animated plot of rabbits' movements."""

    fig = plt.figure(figsize=(7, 7))
    
    global running_time
    running_time = num_of_iterations

    def update(frame_number):
        """Updates the visualization."""

        fig.clear()
        rabbit_count = len(rabbits)
        global running_time
        
        if rabbit_count > 0:
            txt = f"[{frame_number}] There are {rabbit_count} rabbits."
        else:
            txt = "There are no more rabbits."
            running_time = frame_number
            animation.event_source.stop()
            plt.close()
            return
        fig.text(.05,.05,txt)
        plt.imshow(environment, vmin=0, vmax=250)
        
        plt.xlim(0, len(environment))
        plt.ylim(0, len(environment[0]))

        rabbits_interact(rabbits, neighbourhood)

        for agent in rabbits:
            plt.scatter(agent.y, agent.x, c=agent.colour[0])
        
        if save_gif == "YES":
            plt.savefig(os.path.join('output_files','gif',f"{frame_number}.jpg"), quality=100)

    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    plt.show()

    if save_gif == "YES":
        print('Saving model animation as GIF file. This may take some time...')
        gif_file = os.path.join('output_files','gif','saved_animation.gif')
        with imageio.get_writer(gif_file, mode="I", duration=0.1) as writer:
            for file in range(0, running_time):
                image = imageio.imread(os.path.join('output_files','gif',f"{file}.jpg"))
                writer.append_data(image)
                os.remove(os.path.join('output_files','gif',f"{file}.jpg"))
        print(f"GIF was successfully saved in {gif_file}")


