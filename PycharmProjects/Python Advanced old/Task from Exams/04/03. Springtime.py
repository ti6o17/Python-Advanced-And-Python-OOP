def start_spring(**kwargs):
    new_dict = {}
    list_output = []
    for value, key in kwargs.items():
        if key not in new_dict:
            new_dict[key] = []

        new_dict[key].append(value)
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for key in sorted_dict:
        list_output.append(f"{key}:")
        list_output1 = sorted(sorted_dict[key])
        for word in list_output1:
            list_output.append(f"-{word}")
    return '\n'.join(list_output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))
