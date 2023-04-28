from collections import deque


name = input()
name1 = ''
list_names = deque()
# list_customers = []
while not name == 'End':

    # name = input()
    if name == 'Paid':
        while list_names:
            name1 = list_names.popleft()
            print(name1)
    list_names.append(name)
    if "Paid" in list_names:
        list_names.remove("Paid")
    name = input()

print(f"{len(list_names)} people remaining.")
