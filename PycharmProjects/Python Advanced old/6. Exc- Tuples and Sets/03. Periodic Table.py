n = int(input())
elements = ''
list_elements = []
for i in range(n):
    elements += input() + ' '

elements = elements.split()

elements = set(elements)
elements = list(elements)

for element in elements:
    print(element)
