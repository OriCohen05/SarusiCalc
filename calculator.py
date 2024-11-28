from operations import Calculator, Operation

def console_calculator():
    print("Sarusi Calculator!")
    calculator = Calculator()

    while True:
        operation_input = input("Enter operation (ADD, SUBTRACT, MULTIPLY, DIVIDE) or 'exit' to quit: ")
        if operation_input.lower() == 'exit':
            break

        operand1 = float(input("Enter first operand: "))
        operand2 = float(input("Enter second operand: "))

        try:
            operation = Operation[operation_input.upper()]
            result = calculator.calculate(operation, operand1, operand2)
            print(f"Result: {result}")
        except KeyError:
            print("Invalid operation. Please try again.")
        except ValueError as e:
            print(e)