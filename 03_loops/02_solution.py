num = int(input("Enter a number: "))
sum = 0
for i in range(0,num+1,2):
    sum = sum + i
print(f'Sum of all even numbers from 0 to {num} is {sum}')