num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation_type = input("Choose the operation (+, -, *, /):.")

match operation_type:
    case "+":
        result = float(num1) + float(num2)
        print(f"The result is: {result}")
    case "-":
        result = float(num1) - float(num2)
        print(f"The result is: {result}")
    case "*":
        result = float(num1) * float(num2)
        print(f"The result is: {result}")
    case "/":
        if num2 == 0:
            print("MATH ERROR")
        else:
            result = float(num1) / float(num2)
            print(f"The result is: {result}")
    case _: 
        print("invalid operation")