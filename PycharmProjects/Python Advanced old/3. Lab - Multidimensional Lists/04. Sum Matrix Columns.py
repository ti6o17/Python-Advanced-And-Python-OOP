row, column = input().split(', ')
row = int(row)
column = int(column)
matrix = []
list_numbers = []
sum_numbers = 0
sum = 0
for _ in range(row):
    list_numbers = [int(num) for num in input().split(' ')]
    matrix.append(list_numbers)

for j in range(column):
    for i in range(row):
        sum += matrix[i][j]
    print(sum)
    sum = 0