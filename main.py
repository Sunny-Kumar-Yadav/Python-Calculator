# adding calculator logo
from calculator_art import logo
# Add - creating add function
def add(n1, n2):
    return n1 + n2
# Subtract - creating Subtract function
def subtract(n1, n2):
    return n1 - n2
# Multiply - creating Multiply function
def multiply(n1, n2):
    return n1 * n2
#Divide - creating Divide function
def divide(n1, n2):
    return n1 / n2
# Creating a dictionary with the keys of calculation symbols and the values of the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# defining a function 
def calculator():
    # printing the logo
    print(logo)
    # creating input variables
    num1 = float(input("What's the first number?: "))
    # creating a for loop to print out the symbols from the dictionary
    for symbol in operations:
        print(symbol)
    # creating a variable to end the while loop when the user wants to stop
    should_continue = True
    
    while should_continue:
    
        # creating a input variable for the user to choose a symbol from the dictionary
        operation_symbol = input("Pick an operation: ")
        # creating input variables
        num2 = float(input("What's the next number?: "))
        # creating a variable to store the value of the chosen symbol from the dictionary
        calculation_function = operations[operation_symbol]
        # creating a variable to store the solution after running the funtions from the dictionary
        answer = calculation_function(num1, num2)
        # printing the solution in equation format
        print(f"{num1} {operation_symbol} {num2} = {answer} \nYour answer is: {answer}")
        
        # asking user to continue calculation with previous answer
        user_choice =input(f"Type 'y' to continue calculating with {answer} \nType 'n' to start a new calculation:  \nType 'e' to exit. ")
        if user_choice == "y":
            num1 = answer # changing the value of num1 to answer to continue the calculation
        elif user_choice == "n":
            should_continue = False # ending while loop for new calculation
            calculator() # calling the calculator function to start a new calculation
            # calling the  same function withing that function, it'll create a infinite loop
        else:
            should_continue = False # ending while loop for exiting the program
            print(f"Your answer is: {answer},Thankyou for using the calculator \nGoodbye! ")

# calling the calculator function to use it
calculator()
