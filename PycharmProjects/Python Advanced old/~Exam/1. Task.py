from collections import deque

caffeines = deque(input().split(', '))
drinks = deque(input().split(', '))
stamats_coffeine = 0



while caffeines and drinks:
    drink = int(drinks.popleft())
    caffeine = int(caffeines.pop())
    all_caffeine = caffeine * drink
    if (stamats_coffeine + all_caffeine) <= 300:
        stamats_coffeine += all_caffeine
    else:
        drinks.append(str(drink))
        stamats_coffeine -= 30
        if stamats_coffeine < 0:
            stamats_coffeine = 0


if drinks:
    print(f"Drinks left: {', '.join([str(num) for num in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_coffeine} mg caffeine.")
