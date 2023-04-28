n = int(input())
list_reservation = []
for _ in range(n):
    guest_reservation_num = input()
    list_reservation.append(guest_reservation_num)
guest_reservation_num = input()
while not guest_reservation_num == 'END':
    list_reservation.remove(guest_reservation_num)
    guest_reservation_num = input()
list_reservation = set(list_reservation)
print(len(list_reservation))
list_reservation = sorted(list_reservation)
for number in list_reservation:
    print(number)