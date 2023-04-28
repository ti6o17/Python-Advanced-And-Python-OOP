def recursive_power(num, factor):
    # result = 1

    if factor == 0:
        return 1

    return num * recursive_power(num, factor - 1)


print(recursive_power(10, 100))
