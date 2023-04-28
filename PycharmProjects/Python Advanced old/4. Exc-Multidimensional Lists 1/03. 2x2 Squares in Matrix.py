row, columns = input().split()
row = int(row)
columns = int(columns)
matrix = []
for _ in range(row):
    matrix.append(input().split(' '))
count = 0
for i in range(row-1):
    for j in range(columns-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            count += 1
print(count)