def is_inside(row, column, n):
    return 0 <= row < n and 0 <= column < n


def is_knight(row, column, matrix):
    return matrix[row][column] == "K"



n = int(input())
matrix = []
string = ''
list_ = []
for row in range(n):
    string = input()
    for letter in string:
        list_.append(letter)
    matrix.append(list_)
    list_ = []
attacked = 0
max_attacked = 0
flag = True
removed = 0
while flag:
    break_1 = 0
    max_attacked = 0
    for i in range(n):
        for j in range(n):
            attacked = 0
            figure = matrix[i][j]
            if "K" in matrix[i][j]:
                if 0 <= (i - 2) < n and 0 <= (j - 1) < n:
                    if "K" in matrix[i-2][j-1]:
                        attacked += 1
                if 0 <= (i - 2) < n and 0 <= (j + 1) < n:
                    if "K" in matrix[i-2][j+1]:
                        attacked += 1
                if 0 <= (i + 2) < n and 0 <= (j - 1) < n:
                    if "K" in matrix[i+2][j-1]:
                        attacked += 1
                if 0 <= (i + 2) < n and 0 <= (j + 1) < n:
                    if "K" in matrix[i+2][j+1]:
                        attacked += 1
                if 0 <= (i - 1) < n and 0 <= (j + 2) < n:
                    if "K" in matrix[i-1][j+2]:
                        attacked += 1
                if 0 <= (i + 1) < n and 0 <= (j + 2) < n:
                    if "K" in matrix[i+1][j+2]:
                        attacked += 1
                if 0 <= (i - 1) < n and 0 <= (j - 2) < n:
                    if "K" in matrix[i-1][j-2]:
                        attacked += 1
                if 0 <= (i + 1) < n and 0 <= (j - 2) < n:
                    if "K" in matrix[i+1][j-2]:
                        attacked += 1
            if attacked > max_attacked:
                max_attacked = attacked
                attacked = 0
    for i in range(n):
        if break_1 == 1:
            break
        for j in range(n):
            attacked = 0
            figure = matrix[i][j]
            if "K" in matrix[i][j]:
                if 0 <= (i - 2) < n and 0 <= (j - 1) < n:
                    if "K" in matrix[i - 2][j - 1]:
                        attacked += 1
                if 0 <= (i - 2) < n and 0 <= (j + 1) < n:
                    if "K" in matrix[i - 2][j + 1]:
                        attacked += 1
                if 0 <= (i + 2) < n and 0 <= (j - 1) < n:
                    if "K" in matrix[i + 2][j - 1]:
                        attacked += 1
                if 0 <= (i + 2) < n and 0 <= (j + 1) < n:
                    if "K" in matrix[i + 2][j + 1]:
                        attacked += 1
                if 0 <= (i - 1) < n and 0 <= (j + 2) < n:
                    if "K" in matrix[i - 1][j + 2]:
                        attacked += 1
                if 0 <= (i + 1) < n and 0 <= (j + 2) < n:
                    if "K" in matrix[i + 1][j + 2]:
                        attacked += 1
                if 0 <= (i - 1) < n and 0 <= (j - 2) < n:
                    if "K" in matrix[i - 1][j - 2]:
                        attacked += 1
                if 0 <= (i + 1) < n and 0 <= (j - 2) < n:
                    if "K" in matrix[i + 1][j - 2]:
                        attacked += 1
            if attacked == max_attacked:

                x=matrix[i][j]
                matrix[i][j] = '0'
                removed += 1
                # max_attacked = 0
                break_1 = 1

                break
    if max_attacked == 0:
        flag = False
print(removed - 1)

# def is_inside(row, column, n):
#     return 0 <= row < n and 0 <= column < n
#
#
# def is_knight(row, column, matrix):
#     return matrix[row][column] == "K"
#
#
# def get_attack_counter(row, column, matrix):
#     result = 0
#     if is_inside(row-2, column+1, len(matrix)) and is_knight(row-2, column+1, matrix):
#         result += 1
#     if is_inside(row+2, column+1, len(matrix)) and is_knight(row+2, column+1, matrix):
#         result += 1
#     if is_inside(row+2, column-1, len(matrix)) and is_knight(row+2, column-1, matrix):
#         result += 1
#     if is_inside(row-2, column-1, len(matrix)) and is_knight(row-2, column-1, matrix):
#         result += 1
#     if is_inside(row-1, column+2, len(matrix)) and is_knight(row-1, column+2, matrix):
#         result += 1
#     if is_inside(row+1, column+2, len(matrix)) and is_knight(row+1, column+2, matrix):
#         result += 1
#     if is_inside(row-1, column-2, len(matrix)) and is_knight(row-1, column-2, matrix):
#         result += 1
#     if is_inside(row+1, column-2, len(matrix)) and is_knight(row+1, column-2, matrix):
#         result += 1
#
#
# n = int(input())
# matrix = []
# string = ''
# list_ = []
# for row in range(n):
#     string = input()
#     for letter in string:
#         list_.append(letter)
#     matrix.append(list_)
#     list_ = []
# removed_knights = 0
#
# while True:
#     table = {}
#     for row in range(n):
#         for column in range(n):
#             if matrix[row][column] == "0":
#                 continue
#             counter = get_attack_counter(row, column, matrix)
#             table[(row, column)] = counter
#     max_count = 0
#     max_coords = None
#     for coords, counter in table.items():
#         if counter > max_count:
#             max_count = counter
#             max_coords = coords
#
#
#     if len(table) == 0:
#         break
# print(removed_knights)