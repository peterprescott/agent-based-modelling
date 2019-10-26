from sys import argv

DEFAULT_NUM_OF_AGENTS = 25
DEFAULT_LIFESPAN = 50
DEFAULT_NEIGHBOURHOOD = 10
DEFAULT_NUM_OF_ITERATIONS = 10**3

def parameters(cmd_line_input):
    """Read parameters defined from command line,
    or return with defaults if no explicit parameters set."""

    if len(cmd_line_input) < 6:
        animate = "DON'T ANIMATE"
    else: animate = cmd_line_input[5]

    if len(cmd_line_input) < 5:
       num_of_iterations = DEFAULT_NUM_OF_ITERATIONS
    else:
        try:
            num_of_iterations = int(cmd_line_input[4])
        except ValueError:
            num_of_iterations = DEFAULT_NUM_OF_ITERATIONS

    if len(cmd_line_input) < 4:
        neighbourhood = DEFAULT_NEIGHBOURHOOD
    else:
        try:
            neighbourhood = int(cmd_line_input[3])
        except ValueError:
            neighbourhood = DEFAULT_NEIGHBOURHOOD

    if len(cmd_line_input) < 3:
        lifespan = DEFAULT_LIFESPAN
    else:
        try:
            lifespan = int(cmd_line_input[2])
        except ValueError:
            lifespan = DEFAULT_LIFESPAN

    if len(cmd_line_input) < 2:
        num_of_agents = DEFAULT_NUM_OF_AGENTS
    else:
        try:
            num_of_agents = int(cmd_line_input[1])
        except ValueError:
            num_of_agents = DEFAULT_NUM_OF_AGENTS
            try:
                #### Allows you to request animation from terminal
                #### without worrying about setting other parameters.
                if str(cmd_line_input[1][0]).lower() == "a":
                    animate = "ANIMATE"
            except:
                pass

    return(num_of_agents, lifespan, neighbourhood, num_of_iterations, animate)


if __name__ == '__main__':
    print(parameters(argv))
