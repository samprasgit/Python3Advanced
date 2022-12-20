
from functools import wraps 

def welcome(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"Welcome {name}")
            result = func(*args,**kwargs)
            return result
        
        return wrapper
    return decorator


@welcome("Tom")
def my_func(message):
    print(f"Hello {message}")

my_func("Jack")
print(my_func.__name__)
#  my_func

 
    