
matrix = []
list_ = []
row_list = ['a', 'b', 'c', "d", 'e', 'f', 'g', 'h']
column_list = ['8', '7', '6', '5', '4', '3', '2', '1']
for i in range(8):
    list_ = input().split()
    matrix.append(list_)
bcoord = []
wcoord = []
coded_bcoord = []
coded_wcoord = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'b':
            bcoord = [i, j]
            coded_bcoord = [row_list[j],column_list[i]]
        if matrix[i][j] == 'w':
            wcoord = [i, j]
            d=row_list[j]
            e=column_list[i]
            coded_wcoord = [row_list[j], column_list[i]]

if abs(int(bcoord[1]) - int(wcoord[1])) == 1:
    if (int(bcoord[0]) - int(wcoord[0])) % 2 == 0:
        y = int(round(((int(wcoord[0]) - int(bcoord[0])) / 2)))
        print(f"Game over! Black win, capture on {coded_wcoord[0]}{int(coded_wcoord[1]) + y}.")
    else:
        x = int(round(((int(wcoord[0]) - int(bcoord[0])) / 2)))
        print(f"Game over! White win, capture on {coded_bcoord[0]}{int(coded_wcoord[1]) + x + 1}.")
else:
    if (7 - int(bcoord[0])) > int(wcoord[0]):
        print(f"Game over! White pawn is promoted to a queen at {coded_wcoord[0]}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {coded_bcoord[0]}1.")