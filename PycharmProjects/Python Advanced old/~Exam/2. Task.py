n = int(input())
racing_number = input()
count = 0
matrix = []
list_ = []
tunnel1_coords = []
tunnel2_coords = []
for _ in range(n):
    list_ = input().split()
    matrix.append(list_)

for i in range(n):
    for j in range(n):

        if matrix[i][j] == "T":
            count += 1
            if not count == 2:
                tunnel1_coords = [i, j]
            else:
                tunnel2_coords = [i, j]
command = input()
x = 0
y = 0
km = 0
flag = False
while not command == "End":
    if command == "left":
        matrix[x][y] = "."
        y -= 1
        if matrix[x][y] == "T":
            km += 30
            matrix[x][y] = "."
            if x == tunnel1_coords[0] and y == tunnel1_coords[1]:
                x = tunnel2_coords[0]
                y = tunnel2_coords[1]
            else:
                x = tunnel1_coords[0]
                y = tunnel1_coords[1]
            matrix[x][y] = "C"
        elif matrix[x][y] == "F":
            km += 10
            flag = True
            matrix[x][y] = "C"
            break
        else:
            km += 10
            matrix[x][y] = "C"

    elif command == "right":
        matrix[x][y] = "."
        y += 1
        if matrix[x][y] == "T":
            km += 30
            matrix[x][y] = "."
            if x == tunnel1_coords[0] and y == tunnel1_coords[1]:
                x = tunnel2_coords[0]
                y = tunnel2_coords[1]
            else:
                x = tunnel1_coords[0]
                y = tunnel1_coords[1]
            matrix[x][y] = "C"
        elif matrix[x][y] == "F":
            km += 10
            flag = True
            matrix[x][y] = "C"
            break
        else:
            km += 10
            matrix[x][y] = "C"

    elif command == "up":
        matrix[x][y] = "."
        x -= 1
        if matrix[x][y] == "T":
            km += 30
            matrix[x][y] = "."
            if x == tunnel1_coords[0] and y == tunnel1_coords[1]:
                x = tunnel2_coords[0]
                y = tunnel2_coords[1]
            else:
                x = tunnel1_coords[0]
                y = tunnel1_coords[1]
            matrix[x][y] = "C"
        elif matrix[x][y] == "F":
            km += 10
            flag = True
            matrix[x][y] = "C"
            break
        else:
            km += 10
            matrix[x][y] = "C"
    elif command == "down":
        matrix[x][y] = "."
        x += 1
        if matrix[x][y] == "T":
            km += 30
            matrix[x][y] = "."
            if x == tunnel1_coords[0] and y == tunnel1_coords[1]:
                x = tunnel2_coords[0]
                y = tunnel2_coords[1]
            else:
                x = tunnel1_coords[0]
                y = tunnel1_coords[1]
            matrix[x][y] = "C"
        elif matrix[x][y] == "F":
            km += 10
            flag = True
            matrix[x][y] = "C"
            break
        else:
            km += 10
            matrix[x][y] = "C"
    command = input()

if flag:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {km} km.")
for i in range(n):
    print(''.join(matrix[i]))
