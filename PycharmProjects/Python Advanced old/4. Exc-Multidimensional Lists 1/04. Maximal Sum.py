row, columns = input().split()
row = int(row)
columns = int(columns)
matrix = []
for _ in range(row):
    matrix.append([int(num) for num in input().split(' ')])
count = 0
max_sum_matrix = -99999
sum_matrix = 0
max_matrix = []
max_matrix_row1 = []
max_matrix_row2 = []
max_matrix_row3 = []
for i in range(row-2):
    for j in range(columns-2):
        sum_matrix = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1]\
                     + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if sum_matrix > max_sum_matrix:
            max_sum_matrix = sum_matrix
            max_matrix = [
                [matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
                [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],
                [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
            ]
print(f"Sum = {max_sum_matrix}")
for i in range(3):
    print(*max_matrix[i])

