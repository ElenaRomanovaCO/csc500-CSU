# Method to perform calculations
def calculate(num1, num2):
    # Defining addition
    addition = num1 + num2

    # Defining subtraction
    subtraction = num1 - num2

    # Defining multiplication
    multiplication = num1 * num2

    # Defining division
    division = num1 / num2

    return multiplication, division, addition, subtraction

# Main program
def main():
    try:
        # Input from the user
        num1 = float(input("Enter first number (num1): "))
        num2 = float(input("Enter second number (num2): "))

        # Calculating results
        result_multiplication, result_division, result_addition, result_subtraction = calculate(num1, num2)

        # Displaying the results
        print(f"The addition of {num1} and {num2} is: {result_addition}")
        print(f"The subtraction of {num1} by {num2} is: {result_subtraction}")
        print(f"The multiplication of {num1} and {num2} is: {result_multiplication}")
        print(f"The division of {num1} by {num2} is: {result_division}")
    except ValueError:
        print("Invalid input! Please enter a number.", f"{num1=}, {num2}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

if __name__ == "__main__":
    main()
