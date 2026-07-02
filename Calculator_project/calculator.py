from logo import calculator_art
#functions for calculations
def add(n1, n2):
    return  n1 + n2
def subtract(n1, n2):
    return  n1 - n2
def multiply(n1, n2):
    return  n1 * n2
def divide(n1, n2):
    return  n1 / n2

#operation dict
opertions = {"+": add ,
             "-": subtract,
             "*": multiply,
             "/": divide}


print(calculator_art)

def calculate():
    
    num1 = float(input("Enter the first number here: "))
    should_accumlate = True
    while should_accumlate:
        for symbol in opertions:
            print(symbol)
        pick_operation = input("Pick a opertion: ")
        num2 = float(input("Enter the second number here: "))
        result = opertions[pick_operation](num1, num2)
        print(f'{num1} {pick_operation} {num2} = {float(result)}')
        with_result = input(f"Type 'y' for conitue with {result}, or type 'no' for new calculation: ").lower()
        if with_result == "yes":
            num1 = result
        else:
            should_accumlate = False
            print("\n" * 40)
            calculate()
        
calculate()