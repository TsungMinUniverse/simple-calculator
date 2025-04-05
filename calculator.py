def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def main():
    print("Welcome to the Simple Calculator!")
    while(True):
        try:
            a = float(input("The first number: "))
            while(True):
                operator = input("Operator (+, - ,* ,/ ): ")
                if operator in ["+", "-", "*", "/"]:
                    break
                print("Please enter the correct operator!")
            b = float(input("The second number: "))

            if operator == "+":
                print("result: ", add(a, b))
            elif operator == "-":
                print("result: ", subtract(a, b))
            elif operator == "*":
                print("result: ", multiply(a, b))
            elif operator == "/":
                try:
                    print("result: ", divide(a, b))
                except ValueError as e:
                    print(e)
            else:
                print("invalid operator")
        except ValueError as e:
            print("Invalid input. Please enter valid numbers.")
        again = input("continue? (y/n)")
        if again.lower() != "y":
            print("Thanks!")
            break
if __name__ == "__main__":
    main()