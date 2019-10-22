import time
    
def my_timer(process):
    def wrapper():
        ## Start timing.
        start = time.perf_counter()
        
        process()
        
        ## Finish timing.
        end = time.perf_counter()
        time_result = str(end - start)
        return time_result
        
    return wrapper

@my_timer
def do_something():
    print('I am doing something!')
    
print(do_something())
