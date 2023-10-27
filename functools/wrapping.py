"""wrappers are handy when working with decorators"""
from functools import wraps, update_wrapper
import time

def print_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        print(f'Function {f.__name__} took {time.time() - start_time:.2f} seconds to execute')
        return result
    return wrapper

@print_time
def perfect_function():
    """This is a perfect docstring."""
    time.sleep(1)
    print("Finished being perfect")
