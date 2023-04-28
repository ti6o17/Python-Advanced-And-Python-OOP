from collections import deque

elfs_energy = deque(input().split())
materials = deque(input().split())
counter = 0
energy = 0
toys = 0
while elfs_energy and materials:
    counter += 1
    elf_energy = int(elfs_energy.popleft())
    if elf_energy < 5:
        continue
    material = int(materials.pop())
    if counter % 3 == 0 and counter % 5 == 0:
        if elf_energy >= (material * 2):
            energy += material * 2
            elf_energy -= (material * 2)
            elfs_energy.append(str(elf_energy))
            continue
        else:
            materials.append(str(material))
            elf_energy *= 2
            elfs_energy.append(str(elf_energy))
            continue
    if counter % 3 == 0:
        if elf_energy >= (material * 2):
            energy += material * 2
            elf_energy -= (material * 2)
            elf_energy += 1
            toys += 2

            elfs_energy.append(str(elf_energy))
            continue
        else:
            materials.append(str(material))
            elf_energy *= 2
            elfs_energy.append(str(elf_energy))
            continue
    if counter % 5 == 0:
        if elf_energy >= material:
            energy += material
            elf_energy -= material
            elfs_energy.append(str(elf_energy))
            continue
        else:
            materials.append(str(material))
            elf_energy *= 2
            elfs_energy.append(str(elf_energy))
            continue
    if elf_energy >= material:
        energy += material
        elf_energy -= material
        elf_energy += 1
        toys += 1

        elfs_energy.append(str(elf_energy))
    else:
        materials.append(str(material))
        elf_energy *= 2
        elfs_energy.append(str(elf_energy))

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elfs_energy:
    print(f"Elves left: {', '.join(elfs_energy)}")
if materials:
    print(f"Boxes left: {', '.join(materials)}")