string = input("Enter a string: ")

for char in string:
    if string.count(char) == 1:
        print("First Non_Repeated Character is: ", char)
        break