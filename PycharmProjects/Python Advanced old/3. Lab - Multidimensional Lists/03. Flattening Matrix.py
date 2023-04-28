row = int(input())
matrix = []
list_numbers = []
sum_numbers = 0
for _ in range(row):
    list_numbers = [int(num) for num in input().split(', ')]
    matrix += list_numbers
print(matrix)
