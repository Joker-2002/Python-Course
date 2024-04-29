age = int(input("Enter Your age: "))
day  = input("Enter Day:")
price = 12 if age>=18 else 8
if day.lower() == "wednesday":
    price = price - 2
    
print(f"Your Movie Ticket price is: {price}")