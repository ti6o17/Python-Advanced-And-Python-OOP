from collections import deque
n = 5
matrix = []
water = 0
metal = 0
concr = 0
for i in range(6):
    list_ = input().split(' ')
    matrix.append(list_)

que_commands = deque(input().split(', '))
row = 0
column = 0

for i in range(6):
    for j in range(6):
        if matrix[i][j] == 'E':
            row = i
            column = j
while que_commands:
    command = que_commands.popleft()
    if command == 'up':
        row -= 1
        if row < 0:
            row = 5
    elif command == 'left':
        column -= 1
        if column < 0:
            column = 5
    elif command == 'right':
        column += 1
        if column > 5:
            column = 0
    elif command == 'down':
        row += 1
        if row > 5:
            row = 0
    x=matrix[row][column]
    if matrix[row][column] == "W":
        print(f"Water deposit found at ({row}, {column})")
        water += 1
    elif matrix[row][column] == "M":
        print(f"Metal deposit found at ({row}, {column})")
        metal += 1
    elif matrix[row][column] == "C":
        print(f"Concrete deposit found at ({row}, {column})")
        concr += 1
    elif matrix[row][column] == "R":
        print(f"Rover got broken at ({row}, {column})")

        break

if water > 0 and metal > 0 and concr > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")