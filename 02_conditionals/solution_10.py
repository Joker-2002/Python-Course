pet = input("Enter the Type of Pet: ")
age = int(input("Enter Your Pet's Age: "))

if pet.lower() == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("senior dog food")
elif pet.lower() == "cat":
    if age < 2:
        print("kitten food")
    else:
        print("senior cat food")
else:
    print("Invalid Pet")