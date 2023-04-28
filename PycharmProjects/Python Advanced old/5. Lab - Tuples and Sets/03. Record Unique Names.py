n = int(input())
# set_names = set()
list_names = []
for _ in range(n):
    name = input()
    list_names.append(name)

set_names = set(list_names)

for name in set_names:
    print(name)
