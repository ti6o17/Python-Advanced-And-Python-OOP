first, second = input().split(', ')
matrix = []
for _ in range(6):
    matrix.append(input().split(' '))
move = 1
flag_for_first = False
flag_for_second = False
while True:
    indexes = tuple(input())
    i = int(indexes[1])
    j = int(indexes[4])
    if flag_for_first and move % 2 == 1:
        flag_for_first = False
        move += 1
        continue
    if flag_for_second and move % 2 == 0:
        flag_for_second = False
        move += 1
        continue

    if matrix[i][j] == "E":
        if move % 2 == 1:
            print(f"{first} found the Exit and wins the game!")
        else:
            print(f"{second} found the Exit and wins the game!")
        break
    elif matrix[i][j] == "T":
        if move % 2 == 1:
            print(f"{first} is out of the game! The winner is {second}.")
        else:
            print(f"{second} is out of the game! The winner is {first}.")
        break
    elif matrix[i][j] == "W":
        if move % 2 == 1:
            print(f"{first} hits a wall and needs to rest.")
            flag_for_first = True
        else:
            print(f"{second} hits a wall and needs to rest.")
            flag_for_second = True

    move += 1



