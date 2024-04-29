#   DECORATOR PATTERN: ARE BASICALLY TOLL PLAZA. YOU HAVE TO PASS THROUGH IT.
#   Decorators are functions that take another function as an argument, add some kind of functionality and return another function
#   Decorators are a way to modify functions without modifying them

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} time")
        return result
    return wrapper


@timer
def main():
    # time.sleep(n)
    print("hello hello WELCOME!")

# main(9)
main()