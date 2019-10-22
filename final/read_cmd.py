from sys import argv

DEFAULT_NUM_OF_AGENTS = 10
DEFAULT_SIZE_OF_NEIGHBOURHOOD = 10
DEFAULT_NUM_OF_ITERATIONS = 10**4


def parameters(input):
    """Read parameters defined from command line,
    or return with defaults if no explicit parameters set."""
    
    if len(input) < 5:
        animate = "DON'T ANIMATE"
    else: animate = input[4]

    if len(input) < 4:
        num_of_iterations = DEFAULT_NUM_OF_ITERATIONS
    else: 
        try:
            num_of_iterations = int(input[3])
        except:
            num_of_iterations = DEFAULT_NUM_OF_ITERATIONS

    if len(input) < 3:
        neighbourhood = DEFAULT_SIZE_OF_NEIGHBOURHOOD
    else: 
        try:
            neighbourhood = int(input[2])
        except:
            neighbourhood = DEFAULT_SIZE_OF_NEIGHBOURHOOD
        
    if len(input) < 2:
        num_of_agents = DEFAULT_NUM_OF_AGENTS
    else: 
        try:
            num_of_agents = int(input[1])
        except:
            num_of_agents = DEFAULT_NUM_OF_AGENTS
            try:
                #### Allows you to request animation from terminal
                #### without worrying about setting other parameters.
                if str(input[1]).lower() == "a":
                    animate = "ANIMATE"
            except:
                pass
    
    return(num_of_agents, neighbourhood, num_of_iterations, animate)
    
    
if __name__ == '__main__':
    print(parameters(argv))

