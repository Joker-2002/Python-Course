while True:
    ask_num = int(input("Enter a number: "))
    # if ask_num>=1 and ask_num<=10:
    if 1<=ask_num<=10:
        print(f"You entered {ask_num}")
        break
    else:
        print("Invalid Number. Try Again")