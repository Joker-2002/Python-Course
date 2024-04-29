def factorial_recursive(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)
    
print(factorial_recursive(10))