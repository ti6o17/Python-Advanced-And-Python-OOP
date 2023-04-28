from collections import deque
bee_weight_que = deque([int(num) for num in input().split(' ')])
nectar_weight_que = deque([int(num) for num in input().split(' ')])
signs_que = deque([num for num in input().split(' ')])
honey = 0
while bee_weight_que and nectar_weight_que:
    bee_weight = bee_weight_que[0]
    nectar_weight = nectar_weight_que[-1]
    if bee_weight >= nectar_weight:
        nectar_weight = nectar_weight_que.pop()
    else:
        bee_weight = bee_weight_que.popleft()
        nectar_weight = nectar_weight_que.pop()
        sign = signs_que.popleft()
        if sign == "+":
            honey += bee_weight + nectar_weight
        elif sign == "-":
            honey += abs(bee_weight - nectar_weight)
        elif sign == "*":
            honey += bee_weight * nectar_weight
        elif sign == "/":
            honey += bee_weight / nectar_weight
print(f"Total honey made: {honey}")
if bee_weight_que:
    print(f"Bees left: {', '.join(str(num) for num in bee_weight_que)}")
if nectar_weight_que:
    print(f"Nectar left: {', '.join(str(num) for num in nectar_weight_que)}")




