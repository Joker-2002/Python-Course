string = input("Enter a string: ")
reversed_string = ""
# print(f"Reversed String: {string[::-1]}")

# for i in range(len(string)-1, -1, -1):
#     print(string[i], end="")

for char in string:
    reversed_string = char + reversed_string
print(reversed_string)