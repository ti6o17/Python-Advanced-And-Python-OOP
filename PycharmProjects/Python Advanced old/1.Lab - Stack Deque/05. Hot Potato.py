from collections import deque

kids_deque = deque(input().split())
moves = int(input())
kid_left = ''
while kids_deque:
    kids_deque.rotate(-moves)
    kid_left = kids_deque.pop()
    if kids_deque:
        print(f"Removed {kid_left}")
    else:
        break
print(f"Last is {kid_left}")