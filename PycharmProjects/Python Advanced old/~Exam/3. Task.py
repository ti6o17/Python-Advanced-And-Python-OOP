def forecast(*args):
    new_dict = {}
    sorted_new_dict = {}
    list_result = []
    result = ''
    for elem in args:
        new_dict[elem[0]] = []
        new_dict[elem[0]].append(elem[1])
    new_dict = sorted(new_dict.items(), key=lambda x: x[0])
    for key, value in new_dict:
        if value[0] == "Sunny":
            sorted_new_dict[key] = []
            sorted_new_dict[key].append(value)
    for key, value in new_dict:
        if value[0] == "Cloudy":
            sorted_new_dict[key] = []
            sorted_new_dict[key].append(value)
    for key, value in new_dict:
        if value[0] == "Rainy":
            sorted_new_dict[key] = []
            sorted_new_dict[key].append(value)

    for key, value in sorted_new_dict.items():
        value = value[0][0]
        list_result.append(f"{key} - {value}")

    for elem in list_result:
        result += f"{elem}\n"
    return result




print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


