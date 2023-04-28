def shopping_cart(*tuple_):
    new_dict = {'Pizza': [], 'Soup': [], 'Dessert': []}
    dish_list = []
    result = ''
    count_no_ingredients = 0
    for elem in tuple_:
        if not elem == "Stop":
            if elem[0] not in new_dict:
                new_dict[elem[0]] = []
                new_dict[elem[0]].append(elem[1])
            else:
                x = len(new_dict[elem[0]])
                y = new_dict
                if 'Soup' in new_dict and len(new_dict[elem[0]]) < 3:
                    if elem[1] not in new_dict[elem[0]]:
                        new_dict[elem[0]].append(elem[1])
                elif 'Pizza' in new_dict and len(new_dict[elem[0]]) < 4:
                    if elem[1] not in new_dict[elem[0]]:
                        new_dict[elem[0]].append(elem[1])
                elif 'Desert' in new_dict and len(new_dict[elem[0]]) < 2:
                    if elem[1] not in new_dict[elem[0]]:
                        new_dict[elem[0]].append(elem[1])
        else:
            break

    sorted_card = sorted(new_dict.items(), key=lambda z: (-len(z[1]), z[0]))
    print(sorted_card)
    for tuple__ in sorted_card:
        sorted_ingredients = sorted(tuple__[1])
        dish = tuple__[0]
        dish_list.append(dish + ":")
        if sorted_ingredients:
            dish_list.extend(sorted_ingredients)
        else:
            count_no_ingredients += 1
    if count_no_ingredients == 3:
        return 'No products in the cart!'
    else:
        for word in dish_list:
            if ":" in word:
                result += f"{word}"
                result += "\n"
            else:
                result += f" - {word}"
                result += "\n"

    return result


print(shopping_cart(
            ('Pizza', 'ham'),
            ('Dessert', 'milk'),
            ('Pizza', 'ham'),
            'Stop',
))
