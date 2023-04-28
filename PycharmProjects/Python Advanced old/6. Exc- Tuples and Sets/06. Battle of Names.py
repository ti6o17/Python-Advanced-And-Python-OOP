n = int(input())
odd = set()
even = set()
divisor = 0
for _ in range(n):
    name = input()
    sum_ = 0
    divisor += 1
    for letter in name:
        sum_ += int(ord(letter))
    sum_ //= divisor
    if sum_ % 2 == 0:
        even.add(sum_)
    else:
        odd.add(sum_)
sum_odd = sum(odd)
sum_even = sum(even)
if sum_odd == sum_even:
    print(*(odd.union(even)), sep=', ')
elif sum_odd > sum_even:
    print(*(odd.difference(even)), sep=', ')
else:
    print(*(odd.symmetric_difference(even)), sep=', ')