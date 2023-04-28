row = int(input())
matrix = []
list_numbers = []
sum_numbers = 0
for _ in range(row):
    list_numbers = [num for num in input()]
    matrix.append(list_numbers)
symbol = input()
status = False
for i in range(row):
    for j in range(row):
        x = matrix[i][j]
        if matrix[i][j] == symbol:
            print(f'({i}, {j})')
            status = True
            break
    if status:
        break
if not status:
    print(f"{symbol} does not occur in the matrix")
