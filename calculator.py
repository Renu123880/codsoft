def calculator():
    print("Welcome to the Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Input operation choice
        print("Choose an operation:")
        print("Enter + for addition")
        print("Enter - for subtraction")
        print("Enter * for multiplication")
        print("Enter / for division")
        operation = input("Your choice: ")

        # Perform the chosen operation
        if operation == "+":
            result = num1 + num2
            print(f"The result is: {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result is: {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result is: {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is: {result}")
        else:
            print("Invalid operation choice. Please try again.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
