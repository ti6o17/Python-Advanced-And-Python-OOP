from collections import deque
food_quantity = int(input())
# orders = input()
food_list = [int(num) for num in input().split()]

food_deque = deque(food_list)
biggest_order = 0
for order in food_deque:
    if order > biggest_order:
        biggest_order = order
print(biggest_order)


while food_deque:
    executed_order = food_deque[0]
    if executed_order > food_quantity:
        print(f"Orders left:", end=' ')
        print(*food_deque)
        break
    else:
        executed_order = food_deque.popleft()
        food_quantity -= executed_order
if not food_deque:
    print("Orders complete")