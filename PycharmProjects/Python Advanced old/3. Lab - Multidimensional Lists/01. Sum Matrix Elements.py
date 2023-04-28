row, column = input().split(', ')
row = int(row)
column = int(column)
matrix = []
list_numbers = []
sum_numbers = 0
for _ in range(row):
    list_numbers = [int(num) for num in input().split(', ')]
    matrix.append(list_numbers)
    sum_numbers += sum(list_numbers)
print(sum_numbers)
print(matrix)