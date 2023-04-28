row_columns = int(input())
matrix = []
for _ in range(row_columns):
    row = [int(num) for num in input().split(' ')]
    matrix.append(row)
sum_diagonal1 = 0
sum_diagonal2 = 0
for i in range(row_columns):
    j = i
    sum_diagonal1 += matrix[i][j]
for i in range(row_columns):
    j = (row_columns - 1) - i
    sum_diagonal2 += matrix[i][j]
print(abs(sum_diagonal1 - sum_diagonal2))