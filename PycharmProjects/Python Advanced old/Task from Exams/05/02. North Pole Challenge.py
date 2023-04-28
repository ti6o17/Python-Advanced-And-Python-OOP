row, column = input().split(', ')
row = int(row)
column = int(column)
matrix = []
list_row = []
for i in range(row):
    list_row = input().split()
    matrix.append(list_row)
command = input()
coord_i = 0
coord_j = 0
list_christmas_decorations = []
list_gifts = []
list_cookies = []
for i in range(row):
    for j in range(column):
        if matrix[i][j] == 'Y':
            coord_i = i
            coord_j = j
flag = False
while not command == 'End':
    action, steps = command.split('-')
    steps = int(steps)
    if action == 'right':
        for _ in range(steps):
            matrix[coord_i][coord_j] = 'x'
            coord_j += 1
            if coord_j >= column:
                coord_j -= column
            else:
                if matrix[coord_i][coord_j] == "D":
                    list_christmas_decorations.append("D")
                elif matrix[coord_i][coord_j] == "G":
                    list_gifts.append("G")
                elif matrix[coord_i][coord_j] == "C":
                    list_cookies.append("C")
                matrix[coord_i][coord_j] = "Y"
    elif action == 'left':
        for _ in range(steps):
            matrix[coord_i][coord_j] = 'x'
            coord_j -= 1
            if coord_j <= 0:
                coord_j += column
            else:
                if matrix[coord_i][coord_j] == "D":
                    list_christmas_decorations.append("D")
                elif matrix[coord_i][coord_j] == "G":
                    list_gifts.append("G")
                elif matrix[coord_i][coord_j] == "C":
                    list_cookies.append("C")
                matrix[coord_i][coord_j] = "Y"
    if action == 'down':
        for _ in range(steps):
            matrix[coord_i][coord_j] = 'x'
            coord_i += 1
            if coord_i >= row:
                coord_i -= row
            else:
                if matrix[coord_i][coord_j] == "D":
                    list_christmas_decorations.append("D")
                elif matrix[coord_i][coord_j] == "G":
                    list_gifts.append("G")
                elif matrix[coord_i][coord_j] == "C":
                    list_cookies.append("C")
                matrix[coord_i][coord_j] = "Y"
    elif action == 'up':
        for _ in range(steps):
            matrix[coord_i][coord_j] = 'x'
            coord_i -= 1
            if coord_i <= 0:
                coord_i += row
            else:
                if matrix[coord_i][coord_j] == "D":
                    list_christmas_decorations.append("D")
                elif matrix[coord_i][coord_j] == "G":
                    list_gifts.append("G")
                elif matrix[coord_i][coord_j] == "C":
                    list_cookies.append("C")
                matrix[coord_i][coord_j] = "Y"
    count = 0
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 'G' or matrix[i][j] == 'D' or matrix[i][j] == 'C':
                count += 1
                break
    if count == 0:
        flag = True
        break
    command = input()
if flag:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {len(list_christmas_decorations)} Christmas decorations")
print(f"- {len(list_gifts)} Gifts")
print(f"- {len(list_cookies)} Cookies")
for i in range(row):
    print(' '.join(matrix[i]))
