import time
import tracemalloc
import functools

def performance(func):
    """Decorator that measures performance and saves statistics."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Counter
        wrapper.counter += 1
        
        # Memory tracking
        tracemalloc.start()
        
        # Time tracking
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        
        _, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        wrapper.total_time += (end - start)
        wrapper.total_mem += peak_mem
        
        return result
    
    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    
    return wrapper
