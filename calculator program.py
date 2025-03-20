# Basic Calculator Program

# Function to perform the selected operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Input: Get two numbers and operation from the user
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform calculation
        result = calculate(number1, number2, operation)
        
        # Output: Display the result
        if isinstance(result, (int, float)):  # Check if result is a number
            print(f"{number1} {operation} {number2} = {result}")
        else:
            print(result)  # Print error message for invalid operation or division by zero

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the main program
if __name__ == "__main__":
    main()
  #example
calculate(1,4,"*") 