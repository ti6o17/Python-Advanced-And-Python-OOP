def shopping_list(budget, **kwargs):
    budget = int(budget)
    result = []
    count = 0
    if budget < 100:
        result = ("You do not have enough budget.")

        return result
    list_of_goods = len(kwargs) + 1
    for key, value in kwargs.items():
        list_of_goods -= 1
        count += 1
        price, quantity = value
        price = float(price)
        quantity = int(quantity)
        full_price = price * quantity
        if budget < full_price and list_of_goods != 0:
            continue
        elif budget >= full_price:
            budget -= full_price
            result.append(f"You bought {key} for {full_price:.2f} leva.")

        else:
            return '\n'.join(result)
        if count == 5:
            return '\n'.join(result)
    return '\n'.join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
