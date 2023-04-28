def func_executor(*args):
    result = ''
    for function in args:
        result += f"{function[0].__name__} - {function[0](*function[1])}" + '\n'
    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
