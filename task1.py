def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        operation = input("Enter the operation (1/2/3/4): ")
        if operation in {'1', '2', '3', '4'}:
            return operation
        else:
            print("Invalid selection! Please choose 1, 2, 3, or 4.")

def main():
    print("Welcome to the basic calculator!")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        operation = get_operation()

        if operation == '1':
            result = add(num1, num2)
            op_str = "+"
        elif operation == '2':
            result = subtract(num1, num2)
            op_str = "-"
        elif operation == '3':
            result = multiply(num1, num2)
            op_str = "*"
        elif operation == '4':
            result = divide(num1, num2)
            op_str = "/"
        
        print(f"\nThe result of {num1} {op_str} {num2} is: {result}")

        # Check if the user wants to perform another calculation
        cont = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
