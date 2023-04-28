first_seq = set([int(num) for num in input().split()])
second_seq = set([int(num) for num in input().split()])
n = int(input())
for _ in range(n):
    commands = input()
    if not "Check" in commands:
        if "Add" in commands and "First" in commands:
            commands = commands.replace("Add First", '')
            numbers_set = set([int(num) for num in commands.split()])
            first_seq = first_seq.union(numbers_set)
        elif "Add" in commands and "Second" in commands:
            commands = commands.replace("Add Second", '')
            numbers_set = set([int(num) for num in commands.split()])
            second_seq = second_seq.union(numbers_set)
        elif "Remove" in commands and "First" in commands:
            commands = commands.replace("Remove First", '')
            numbers_set = set([int(num) for num in commands.split()])
            first_seq = first_seq.difference(numbers_set)
        elif "Remove" in commands and "Second" in commands:
            commands = commands.replace("Remove Second", '')
            numbers_set = set([int(num) for num in commands.split()])
            second_seq = second_seq.difference(numbers_set)
    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print("True")
        else:
            print("False")
first_seq = sorted(first_seq)
second_seq = sorted(second_seq)
print(*first_seq, sep=", ")
print(*second_seq, sep=", ")