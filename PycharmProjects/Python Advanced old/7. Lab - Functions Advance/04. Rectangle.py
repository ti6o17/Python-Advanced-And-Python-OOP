def rectangle(*args):
    a = args[0]
    b = args[1]

    def perimeter():
        return (a + b) * 2

    def area():
        return a * b

    if not isinstance(a, int) or not isinstance(b, int):
        result = "Enter valid values!"
    else:
        result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

    return result


print(rectangle(2, 10))
