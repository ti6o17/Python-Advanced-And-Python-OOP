from collections import deque

parentheses = input()
deque_parentheses = deque()
flag = True
par1 = ''
par2 = ''

for i in range(len(parentheses)):
    deque_parentheses.append(parentheses[i])

if not deque_parentheses:
    print('NO')
elif len(parentheses) % 2 != 0:
    print('NO')
else:
    while deque_parentheses:
        par1 = deque_parentheses.popleft()
        if par1 == '(':
            par2 = deque_parentheses[0]
            if par2 != ')':
                par2 = deque_parentheses[-1]
                if par2 != ')':
                    print("NO")
                    flag = False
                    break
                else:
                    deque_parentheses.pop()
            else:
                deque_parentheses.popleft()
        elif par1 == '[':
            par2 = deque_parentheses[0]
            if par2 != ']':
                par2 = deque_parentheses[-1]
                if par2 != ']':
                    print("NO")
                    flag = False
                    break
                else:
                    deque_parentheses.pop()
            else:
                deque_parentheses.popleft()
        elif par1 == '{':
            par2 = deque_parentheses[0]
            if par2 != '}':
                par2 = deque_parentheses[-1]
                if par2 != '}':
                    print("NO")
                    flag = False
                    break
                else:
                    deque_parentheses.pop()
            else:
                deque_parentheses.popleft()
    if flag:
        print('YES')
