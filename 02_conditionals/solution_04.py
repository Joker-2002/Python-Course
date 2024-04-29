color = input("Enter Your Fruit Color: ")

if color.lower() == "green":
    print("Unripe")
elif color.lower() == "yellow":
    print("Ripe")
elif color.lower() == "brown":
    print("Overripe")
else:
    print("Rotten")