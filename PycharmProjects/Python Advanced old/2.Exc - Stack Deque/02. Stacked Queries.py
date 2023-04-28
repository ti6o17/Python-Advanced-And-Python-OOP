n = int(input())
stack = []
max_num = -999999
min_num = 999999
for _ in range(n):
    command = input()
    if command == "2":
        if stack:
            stack.pop()
        else:
            continue

    elif command == '3':
        if stack:
            for num in stack:
                if num >= max_num:
                    max_num = num
            print(max_num)
            max_num = -999999
        else:
            continue
    elif command == '4':
        if stack:
            for num in stack:
                if num <= min_num:
                    min_num = num
            print(min_num)
            min_num = 999999
        else:
            continue
    else:
        _, number = command.split(' ')
        number = int(number)
        stack.append(number)

rev_stack = reversed(stack)
print(', '.join([str(num) for num in rev_stack]))