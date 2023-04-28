from collections import deque
input_string = deque(input().split())
nums_to_calculate = []
sign = ''
num0 = 0
num1 = 1
flag = 0

while input_string:
    element = (input_string.popleft())
    if element.isdigit():
        nums_to_calculate.append(int(element))
        continue
    else:
        sign = element

    if sign == "+":
        for num in nums_to_calculate:
            num0 += num
            flag = 1
    elif sign == "-":
        for num in nums_to_calculate:
            if flag == 0:
                num0 += num
                flag = 1
            else:
                num0 -= num
    elif sign == "*":
        for num in nums_to_calculate:
            if flag == 0:
                num0 = num1
                num0 *= num
                flag = 1
            else:
                num0 *= num
    elif sign == "/":
        for num in nums_to_calculate:
            if flag == 0:
                num0 = num1
                num0 *= num
                flag = 1
            else:
                num0 //= num
    nums_to_calculate = []
print(num0)