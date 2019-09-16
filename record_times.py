import random
import operator
import matplotlib.pyplot
import time

iterations = [10, 100, 1000, 10000, 100000, 1000000]

iterations_vs_time = []

def record_time(iterations):
    start = time.perf_counter()
    
    
    num_of_agents = 10
    num_of_iterations = iterations
    agents = []
    
    # Make the agents.
    for i in range(num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
    
            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100
    
            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100
    
    distances = []
    
    def distance_between(m,n):
        distance_squared = (agents[m][1]-agents[n][1])**2 + (agents[m][0]-agents[n][0])**2
        distance = distance_squared**(1/2)
        distances.append(distance)
        return distance
        
    
    for i in range(num_of_agents - 1):
        for j in range (i + 1, num_of_agents):
            print(distance_between(i,j))
    
    end = time.perf_counter()

    # print time taken for calculations
    time_taken = end - start
    print("time = " + str(time_taken))
    
    iterations_vs_time.append([iterations, time_taken])    
    
    return [iterations, time_taken]
    
for i in iterations:
    record_time(i)

print(iterations_vs_time)
    
# show scatter graph
matplotlib.pyplot.ylim(0, 10)
matplotlib.pyplot.xlim(0, max(iterations)*2)
for i in iterations_vs_time:
    matplotlib.pyplot.scatter(i[0],i[1])
matplotlib.pyplot.show()


