#   DECORATOR PATTERN: ARE BASICALLY TOLL PLAZA. YOU HAVE TO PASS THROUGH IT.
#   Decorators are functions that take another function as an argument, add some kind of functionality and return another function
#   Decorators are a way to modify functions without modifying them.

import time

def cache(func):
    cache_value = {}
    def wrapper(*args,**kwargs):
        if args in cache_value:
            print("Fetching from cache")
            return cache_value[args]
        else:
            print("Calculating result")
            result = func(*args,**kwargs)
            cache_value[args] = result
            return result
    return wrapper

@cache
def add(x,y):
    time.sleep(3)
    return x+y

print(add(10,29))
print(add(10,99))
print(add(10,29))
print(add(10,29))
print(add(10,19))
print(add(10,9))
print(add(10,29))
