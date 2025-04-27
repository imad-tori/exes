def calculator():
    first_num = int(input("enter the first number: "))
    second_num = int(input("enter the second number: "))
    math_operation = input("enter math operation: ")

    if math_operation == "+":
        print(first_num + second_num)
    elif math_operation == "-":
        print(first_num - second_num)
    elif math_operation == "*":
        print(first_num * second_num)
    elif math_operation == "/":
        print(first_num / second_num)
    elif math_operation == "**":
        print(first_num ** second_num)
    else:
        print("invalid math operation")

calculator()