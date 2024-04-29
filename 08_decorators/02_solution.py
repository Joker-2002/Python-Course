#   DECORATOR PATTERN: ARE BASICALLY TOLL PLAZA. YOU HAVE TO PASS THROUGH IT.
#   Decorators are functions that take another function as an argument, add some kind of functionality and return another function
#   Decorators are a way to modify functions without modifying them

import time

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} : {v}" for k,v in kwargs.items())
        print(f"Function name: {func.__name__} Args value: ({args_value}) Kwargs value: ({kwargs_value})")
        return func(*args,**kwargs)
    return wrapper


@debug
def greet(name,greeting = "Namaste!!"):
    print(f"{greeting} {name}")

greet("Debasish")
greet("Debashree",greeting = "Hello Ji Hello!!")