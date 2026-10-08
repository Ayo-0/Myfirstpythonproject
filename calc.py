def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide

}

def calculator():
    should_continue = False

    num_1 = float(input("What is the first number?: "))

    while not should_continue:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What operation do you want to perform?: ")
        num_2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        choice = input(f"Type 'y' to vontinue calculating with {answer} or type 'n' to start a new calculation: \n" )

        if choice == "y":
            num_1 = answer 
        else:
            should_continue = True
            print("\n" * 20)
            calculator()

calculator()