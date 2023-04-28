
row, column = input().split(', ')
row = int(row)
column = int(column)
matrix = []
list_numbers = []
sum_numbers = 0
max_sum = -9999
for _ in range(row):
    list_numbers = [num for num in input().split(', ')]
    matrix.append(list_numbers)
sub_matrix = []
max_sub_matrix = []
for i in range(row - 1):
    sum_numbers = 0
    sub_matrix.clear()
    for j in range(column - 1):
        sum_numbers = 0
        sub_matrix.clear()
        sub_matrix.append(matrix[i][j])
        sum_numbers += int(matrix[i][j])
        sub_matrix.append(matrix[i][j+1])
        sum_numbers += int(matrix[i][j+1])
        sub_matrix.append(matrix[i+1][j])
        sum_numbers += int(matrix[i+1][j])
        sub_matrix.append(matrix[i+1][j+1])
        sum_numbers += int(matrix[i+1][j+1])
        if sum_numbers > max_sum:
            max_sub_matrix.clear()
            max_sum = sum_numbers
            max_sub_matrix = sub_matrix.copy()

print(max_sub_matrix[0], end=' ')
print(max_sub_matrix[1])
print(max_sub_matrix[2], end=' ')
print(max_sub_matrix[3])
print(max_sum)



