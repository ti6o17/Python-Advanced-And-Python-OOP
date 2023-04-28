"""
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""
n = int(input())
matrix = []
list_ = []
for row in range(n):
    matrix.append([int(num) for num in input().split()])
command = input()
while "END" not in command:
    if "Add" in command:
        command = command.replace("Add ", "")
        # command = command.replace(" ","")
        row, column, value = command.split()
        if n > int(row) >= 0 and n > int(column) >= 0:
            matrix[int(row)][int(column)] += int(value)
        else:
            print('Invalid coordinates')
    elif "Subtract" in command:
        command = command.replace("Subtract ", "")
        row, column, value = command.split()
        if n > int(row) >= 0 and n > int(column) >= 0:
            matrix[int(row)][int(column)] -= int(value)
        else:
            print('Invalid coordinates')
    command = input()
for row in matrix:
    print(*row)