num = int(input("Enter a number to check: "))
isPrime = True

if num>1:
    for i in range(2,num):
        if num%i == 0:
            isPrime = False
            break
# print(isPrime)

if isPrime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")