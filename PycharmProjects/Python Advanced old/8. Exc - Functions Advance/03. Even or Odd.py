def even_odd(*args):
    list_ = []
    for i in range(len(args) - 1):
        list_.append(int(args[i]))
    arg = 0 if args[-1] == "even" else 1
    even_odd_list = [num for num in list_ if num % 2 == arg]
    return even_odd_list


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))