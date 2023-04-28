n = int(input())
names = []

for _ in range(n):
    names.append(input())

names = set(names)
names = list(names)

for i in range(len(names)):
    print(names[i])