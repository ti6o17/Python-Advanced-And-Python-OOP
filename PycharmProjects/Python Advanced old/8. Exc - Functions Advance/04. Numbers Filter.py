def even_odd_filter(**kwargs):
    odd_list = []
    even_list = []
    numbers = {}
    for key in kwargs:
        if key == "odd":
            odd_list = [int(num) for num in kwargs['odd']]
            numbers["odd"] = [num for num in odd_list if num % 2 == 1]
        else:
            even_list = [int(num) for num in kwargs['even']]
            numbers["even"] = [num for num in even_list if num % 2 == 0]

    return dict(sorted(numbers.items(), key=lambda x: len(x[1]), reverse=True))



print(even_odd_filter(
    even=[2, 2, 30, 44, 10, 5],
))

