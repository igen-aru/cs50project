def main():
    expression = input("Enter an arithmetic expression (x y z): ").strip()
    x_str, operator, z_str = expression.split()
    x = int(x_str)
    z = int(z_str)
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z == 0:
            print("Error: Division by zero")
            return
        result = x / z
    else:
        print("Error: Invalid operator")
        return
    print(f"{result:.1f}")

main()
