from collections import deque

bottle_water = int(input())
names = deque()
name = input()
while name != 'Start':
    names.append(name)
    name = input()
water_taken_received = input()
name_taken = ''
while water_taken_received != "End":
    water_taken_received.isdigit()
    if water_taken_received.isdigit():
        water_taken_received = int(water_taken_received)
        prev_water = bottle_water
        bottle_water -= water_taken_received
        if bottle_water >= 0:
            name_taken = names.popleft()
            print(f'{name_taken} got water')
        else:
            name_taken = names.popleft()
            print(f"{name_taken} must wait")
            bottle_water = prev_water
    else:
        _, liters = water_taken_received.split()
        liters = int(liters)
        bottle_water += liters
    water_taken_received = input()
print(f"{bottle_water} liters left")
