from collections import deque
row, column = input().split(' ')
row = int(row)
column = int(column)
string = input()
que = deque()
list_ = []
matrix = []
count1 = 0
count2 = len(string)-1
for i in range(row):
    for j in range(column):
        if i % 2 == 0:
            if count1 <= count2:
                que.append(string[count1])
                list_ = list(que)
                count1 += 1
            else:
                count1 = 0
                que.append(string[count1])
                list_ = list(que)
                count1 += 1
        else:
            if count1 <= count2:
                que.appendleft(string[count1])
                list_ = list(que)
                count1 += 1
            else:
                count1 = 0
                que.appendleft(string[count1])
                list_ = list(que)
                count1 += 1
    matrix.append(list_)
    list_ = []
    que = deque()
for i in range(row):
    print(*matrix[i], sep='')