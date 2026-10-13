current = 0
print("Simple Calculator")
print("Operators: + - * / \\ ^ %   C = clear   OFF = turn off")

while True:
    print("Display:", current)
    op = input("Operator: ").strip().upper()

    if op == "OFF":
        print("Calculator off")
        break
    elif op == "C":
        current = 0
        print("Cleared")
    elif op in ["+", "-", "*", "/", "\\", "^", "%"]:
        try:
            n = float(input("Number: "))
        except ValueError:
            print("Not a valid number")
            continue

        if op in ["/", "\\", "%"] and n == 0:
            print("Cannot divide by zero")
            continue

        if op == "+":
            current = current + n
        elif op == "-":
            current = current - n
        elif op == "*":
            current = current * n
        elif op == "/":
            current = current / n
        elif op == "\\":
            current = current // n
        elif op == "%":
            current = current % n
        else:
            current = current ** n

        # drop the .0 on whole numbers
        if isinstance(current, float) and current == int(current):
            current = int(current)
    else:
        print("Invalid operator")