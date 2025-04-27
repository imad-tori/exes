

while True:

    user_input = input("enter number to check even or odd, enter exit to exit: ")

    if user_input == "exit":
        break
    
    if user_input.isdigit():
        number = int(user_input)
    else:
        continue

    if number % 2 == 0:
        print("even")
    else:
        print("odd")