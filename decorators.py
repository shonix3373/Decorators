
import time

def my_timer(orig_function):
    
    import time 
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print("function {} ran in {} seconds.".format(orig_function.__name__, t2))
        return(result)
 
        
    return(wrapper)  

 # Original function
@my_timer
def cube(num):
    time.sleep(1)
    return(num*num*num)

print(cube(3))