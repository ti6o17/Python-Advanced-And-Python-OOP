numbers = [int(num) for num in input().split()]

positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]

print(sum(negative_nums))
print(sum(positive_nums))

if sum(positive_nums) > abs(sum(negative_nums)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")