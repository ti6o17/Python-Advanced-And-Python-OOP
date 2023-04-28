from collections import deque

materials = deque(int(num) for num in input().split())
magic_levels = deque(int(num) for num in input().split())

dict_toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
list_present = []
work_done1 = {"Doll", "Wooden train"}
work_done2 = {"Teddy bear", 'Bicycle'}
while materials and magic_levels:
    material = materials[-1]
    magic_level = magic_levels[0]
    operation = material * magic_level
    if operation in dict_toys:
        material = materials.pop()
        magic_level = magic_levels.popleft()
        list_present.append(dict_toys[operation])
    elif material == 0:
        material = materials.pop()
    elif magic_level == 0:
        magic_level = magic_levels.popleft()
    elif operation < 0:
        operation = material + magic_level
        material = materials.pop()
        magic_level = magic_levels.popleft()
        materials.append(operation)
    elif operation not in dict_toys:
        magic_level = magic_levels.popleft()
        material = materials.pop() + 15
        materials.append(material)



set_present = set(list_present)
if work_done1.issubset(set_present) or work_done2.issubset(set_present):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(str(toy) for toy in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(toy) for toy in magic_levels)}")
set_present = sorted(set_present)
for toy in set_present:
    print(f"{toy}: {list_present.count(toy)}")

