n = int(input())
list_car_num = []
for _ in range(n):
    in_out, car_num = input().split(', ')
    if in_out == 'IN':
        list_car_num.append(car_num)
    else:
        list_car_num.remove(car_num)
set_car_num = set(list_car_num)

if set_car_num:
    for number in set_car_num:
        print(number)
else:
    print("Parking Lot is Empty")