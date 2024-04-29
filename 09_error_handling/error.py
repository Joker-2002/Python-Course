# with open("youtube.txt","w") as file:
#     file.write("Chai Aur Code!!!")

# try:
#     with open("youtube.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File Not Found")
# except Exception as e:
#     print(e)
# finally: # act as default case.
#     print("file found")
#     file.close()


file = open("youtube.txt","r")
print(file.read())

file.close()

