clothes = [int(item) for item in input().split()]
rack_volume = int(input())
empty_rack_volume = rack_volume
number_racks = 1
num = 0
clothes_rack = 0
while clothes:
    cloth = clothes.pop()
    # clothes_rack += cloth
    rack_volume -= cloth
    if rack_volume > 0:
        continue
    elif rack_volume == 0:
        rack_volume = empty_rack_volume
        if clothes:
            number_racks += 1
    else:
        rack_volume = empty_rack_volume
        clothes.append(cloth)
        number_racks += 1
print(number_racks)

