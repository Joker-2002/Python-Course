x = 10012
def func1():
    # x = 100
    def func2():
        y = 200
        # x = 900
        # print(x)
        def func3():
            # x = 120
            return x
        return func3
    return func2 
   
# print(func1())
res = func1()
# print(res())
newRes = res()
print(newRes())

# print(x)