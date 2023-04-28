# from collections import deque
expression = input()
index = 0
list_open_parentheses = []
list_close_parentheses = []
index_open = 0
index_close = 0
for letter in expression:
    index += 1
    if letter == "(":
        list_open_parentheses.append(index)
    elif letter == ')':
        list_close_parentheses.append(index)

        index_open = list_open_parentheses.pop()
        index_close = list_close_parentheses.pop()
        print(f'{expression[(index_open - 1):index_close]}')
