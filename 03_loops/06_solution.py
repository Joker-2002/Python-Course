num = int(input("Enter a number: "))
factorial = 1
while num>0:
    factorial = factorial * num
    num = num - 1
print("The factorial of the number is: ",factorial)
