n = 6
matrix = []
for _ in range(6):
    matrix.append(input().split(' '))
start_index = tuple(input())

i = int(start_index[1])
j = int(start_index[4])

command_sentence = input()
while command_sentence != 'Stop':
    if 'Create' in command_sentence:
        command, direction, value = command_sentence.split(', ')

        if direction == "up":
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1

        if matrix[i][j] == ".":
            matrix[i][j] = value
    elif 'Update' in command_sentence:
        command, direction, value = command_sentence.split(', ')

        if direction == "up":
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1
        if not matrix[i][j] == ".":
            matrix[i][j] = value
    elif 'Delete' in command_sentence:
        command, direction = command_sentence.split(', ')
        if direction == "up":
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1
        matrix[i][j] = '.'
    elif 'Read' in command_sentence:
        command, direction = command_sentence.split(', ')
        if direction == "up":
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1
        if not matrix[i][j] == ".":
            print(matrix[i][j])
    command_sentence = input()

for x in range(len(matrix)):
    print(*matrix[x])