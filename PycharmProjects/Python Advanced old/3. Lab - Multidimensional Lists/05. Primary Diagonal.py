row = int(input())
matrix = []
list_numbers = []
sum_numbers = 0
for _ in range(row):
    list_numbers = [int(num) for num in input().split(' ')]
    matrix.append(list_numbers)
for i in range(row):
    # j = i
    sum_numbers += matrix[i][i]
print(sum_numbers)