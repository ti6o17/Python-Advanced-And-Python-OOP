indexes = input().split(' ')
row = int(indexes[0])
column = int(int(indexes[1]))
matrix = []
for i in range(row):
    matrix.append([num for num in input().split()])
command = input()
# flag = True
while not command == "END":
    if "swap" in command:
        coordinates = command.replace("swap ", "")
        list_coordinates = [int(num) for num in coordinates.split(' ')]
        if list_coordinates[0] > row or list_coordinates[2] > row or list_coordinates[1] > column or list_coordinates[3] > column or (list_coordinates[0] < 0 or list_coordinates[2] < 0 or list_coordinates[1] < 0 or list_coordinates[3]) < 0:
            # flag = False
            print("Invalid input!")
        elif not len(list_coordinates) == 4:
            print("Invalid input!")
        else:
            num1 = matrix[list_coordinates[0]][list_coordinates[1]]
            num2 = matrix[list_coordinates[2]][list_coordinates[3]]
            matrix[list_coordinates[0]][list_coordinates[1]] = num2
            matrix[list_coordinates[2]][list_coordinates[3]] = num1
            for i in range(row):
                print(*matrix[i])

    else:
        print("Invalid input!")

    command = input()
