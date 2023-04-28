from collections import deque
tank = 0
stations = int(input())
que_petrol = deque()
que_distance = deque()
old_tank = 0
station_number = 0
station_to_go = 0
for _ in range(stations):
    petrol1, distance1 = input().split()
    que_petrol.append(int(petrol1))
    que_distance.append(int(distance1))
flag = False
for station_to_check in range(stations):
    tank = 0
    if not flag:
        for station in range(stations):
            old_tank = tank
            tank += int(que_petrol[station])
            if tank < int(que_distance[station]):
                que_distance.rotate(-1)
                que_petrol.rotate(-1)
                tank = old_tank
                break
            else:
                tank -= int(que_distance[station])
                flag = True
                station_to_go = station_to_check
                continue
    else:
        break
print(station_to_go)

