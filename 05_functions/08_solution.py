def print_kwargs(**kwargs):
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(a=1,b=2,c=4)
print_kwargs(Name="Rahul",Job="Private",Salary="300000")