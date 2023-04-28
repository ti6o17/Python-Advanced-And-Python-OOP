row, column = input().split(' ')
row = int(row)
column = int(column)
matrix = []
list_from_m = []
for i in range(row):
    for j in range(column):
        list_from_m.append(f"{chr(97+i)}{chr(97+i+j)}{chr(97+i)}")
    matrix.append(list_from_m)
    list_from_m = []
for i in range(row):
    print(*matrix[i])