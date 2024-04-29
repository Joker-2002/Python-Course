def generator_even(limit):
    for i in range(2,limit+1,2):
        # return i
        yield i
    
# print(generator_even(10))
for num in generator_even(100):
    print(num)