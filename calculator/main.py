def calculate(a: float, op: str, b: float):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


def parse_expression(raw: str) -> tuple[float, str, float]:
    s = raw.strip()
    if not s:
        raise ValueError("Empty expression")

    ops = ["+", "-", "*", "/"]
    op_index = -1
    op_found = None
    for op in ops:
        idx = s.find(op)
        if idx > 0:
            op_index = idx
            op_found = op
            break
    if op_found is None:
        raise ValueError("No valid operator found")

    left = s[:op_index].strip()
    right = s[op_index + 1 :].strip()
    if left == "" or right == "":
        raise ValueError("Invalid expression format")

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("Operands must be numbers")

    if op_found == "/" and b == 0:
        raise ValueError("Cannot divide by zero")

    return a, op_found, b


def repl():
    print("Welcome to the calculator! Type 'exit' to quit.")
    while True:
        raw = input("> ")
        if raw.strip().lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        try:
            a, op, b = parse_expression(raw)
            result = calculate(a, op, b)
            print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    repl()
