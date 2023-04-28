def operate(operator, *args):
    a = 0
    b = 1
    if operator == "+":

        for num in args:
            a += num
        return a
    elif operator == "-":
        for num in args:
            a -= num
        return a
    elif operator == "*":
        for num in args:
            b *= num
        return b
    elif operator == "/":
        a, b = args
        c = a / b
        return c


print(operate("/", 18, 3))