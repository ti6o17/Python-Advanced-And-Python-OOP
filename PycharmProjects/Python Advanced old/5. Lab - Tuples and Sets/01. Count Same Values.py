numbers = [float(num) for num in input().split()]
numbers_tuples = tuple(numbers)
numbers_sets = numbers
while numbers:
    print(f'{numbers[0]} - {numbers_tuples.count(numbers[0])} times')
    check_num = numbers[0]
    while check_num in numbers:
        numbers.remove(check_num)

