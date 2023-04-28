from collections import deque
chocolate_deque = deque([int(num) for num in input().split(', ')])
milk_deque = deque([int(num) for num in input().split(', ')])
milkshake = 0
flag = True
while flag and chocolate_deque and milk_deque:
    chocolate = chocolate_deque[-1]
    milk = milk_deque[0]
    if chocolate == milk:
        chocolate = chocolate_deque.pop()
        milk = milk_deque.popleft()
        milkshake += 1
        if milkshake == 5:
            flag = False
    elif chocolate <= 0:
        chocolate = chocolate_deque.pop()
    elif milk <= 0:
        milk = milk_deque.popleft()
    else:
        milk_deque.rotate(-1)
        chocolate = chocolate_deque.popleft() - 5
        chocolate_deque.append(chocolate)

if not flag:
    print("Great! You made all the chocolate milkshakes needed!")
    if chocolate_deque:
        print(f"Chocolate: {', '.join(str(num) for num in chocolate_deque)}")
    else:
        print("Chocolate: empty")
    if milk_deque:
        print(f"Milk: {', '.join(str(num) for num in milk_deque)}")
    else:
        print("Milk: empty")
else:
    print("Not enough milkshakes.")
    if chocolate_deque:
        print(f"Chocolate: {', '.join(str(num) for num in chocolate_deque)}")
    else:
        print("Chocolate: empty")
    if milk_deque:
        print(f"Milk: {', '.join(str(num) for num in milk_deque)}")
    else:
        print("Milk: empty")


