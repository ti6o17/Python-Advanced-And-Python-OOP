def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for key, item in sorted_dict:
        item = sorted(item, reverse=True)
        result += key + '\n'
        result += '\n'.join([str(x) for x in item]) + '\n'
    return result
    # sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
