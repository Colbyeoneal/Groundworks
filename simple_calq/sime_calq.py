def main():
    print("Welcome to the 2-Digit Calculator!")
    print("This calculator accepts two 2-digit numbers and performs +, -, *, or / operations.")

    # Get first number
    while True:
        try:
            num1 = int(input("Enter the first 2-digit number (10-99): "))
            if 10 <= num1 <= 99:
                break
            else:
                print("Please enter a number between 10 and 99.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get second number
    while True:
        try:
            num2 = int(input("Enter the second 2-digit number (10-99): "))
            if 10 <= num2 <= 99:
                break
            else:
                print("Please enter a number between 10 and 99.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2  # Use float division

    # Display result
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()