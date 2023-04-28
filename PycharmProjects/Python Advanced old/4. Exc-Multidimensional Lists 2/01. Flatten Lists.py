# 1 2 3 |4 5 6 |  7  88
from collections import deque
input_ = input().split()
input_ = " ".join(input_)
# input_ = " ".join(input().split())

# input_ = input_.replace("  ", " ")
# input_ = input_.replace("   ", " ")
input_ = input_.replace(' |', '|')
input_ = input_.replace('| ', '|')
matrix = deque()
list_ = input_.split('|')
for row in list_:
    matrix.appendleft(row)

print(*matrix)