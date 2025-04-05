def add(a, b):
    return a + b

def substrate(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "b shouldn't be 0"
    return a / b

def main():
    print("welcome!")
    a = float(input("The first number: "))
    operator = input("Operator (+, - ,* ,/ ): ")
    b = float(input("The second number: "))

    if operator == "+":
        print("result: ", add(a, b))
    elif operator == "-":
        print("result: ", substrate(a, b))
    elif operator == "*":
        print("result: ", multiply(a, b))
    elif operator == "/":
        print("result: ", divide(a, b))
    else:
        print("invalid operator")

if __name__ == "__main__":
    main()