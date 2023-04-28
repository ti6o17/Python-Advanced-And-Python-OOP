row_columns = int(input())
matrix = []
# row = []
for _ in range(row_columns):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)
# print(matrix)
sum_diagonal1 = 0
list_sum_diagonal1 = []
sum_diagonal2 = 0
list_sum_diagonal2 = []
for i in range(row_columns):
    j = i
    sum_diagonal1 += matrix[i][j]
    list_sum_diagonal1.append(matrix[i][j])

for i in range(row_columns):
    j = (row_columns - 1) - i
    sum_diagonal2 += matrix[i][j]
    list_sum_diagonal2.append(matrix[i][j])
print("Primary diagonal:", end=' ')
print(*list_sum_diagonal1, sep=', ', end='')
print(f". Sum: {sum_diagonal1}")
print(f"Secondary diagonal: {', '.join(str(num) for num in list_sum_diagonal2)}. Sum: {sum_diagonal2} ")
