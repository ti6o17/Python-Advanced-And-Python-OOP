from collections import deque

seats_sequence = deque(input().split(", "))
first_row = deque(input().split(", "))
second_row = deque(input().split(", "))
seat_match = 0
seat_matched = []
rotations = 0
while True:
    number_1st_row = first_row.popleft()
    number_2nd_row = second_row.pop()
    checked_number = int(number_1st_row) + int(number_2nd_row)
    checked_letter = chr(checked_number)
    checked_seat1 = number_1st_row + checked_letter
    checked_seat2 = number_2nd_row + checked_letter
    if checked_seat1 in seats_sequence:
        seat_matched.append(checked_seat1)
        seats_sequence.remove(checked_seat1)
        seat_match += 1
    elif checked_seat2 in seats_sequence:
        seat_matched.append(checked_seat2)
        seats_sequence.remove(checked_seat2)
        seat_match += 1
    else:
        first_row.append(number_1st_row)
        second_row.appendleft(number_2nd_row)

    rotations += 1
    if seat_match == 3 or rotations == 10:
        break

print(f"Seat matches: {', '.join(seat_matched)}")
print(f"Rotations count: {rotations}")
