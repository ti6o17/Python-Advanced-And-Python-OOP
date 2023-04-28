# n = int(input())
# p = 0
# count = 1
# if n % 2 == 0:
#     print("No")
# else:
#     for p in range(1, int(n/2)):
#         x = n % p
#         if n % p == 0:
#             count += 1
#     if count > 2:
#         print("No")
#     else:
# #         print("Yes")
# #
# def Solve(N):
#     count = 0
#     if N % 2 == 0:
#         return "NO"
#     else:
#         for i in range(1, int(N / 2)):
#             if N % i == 0:
#                 count += 1
#         if count > 2:
#             return 'NO'
#         else:
#             return 'YES'
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     out_ = Solve(N)
#     print(out_)
from random import sample

sample_list = ["luxuriant", "silly", "dizzy", "frightening", "blink", "silly", "enjoy","suspend", "blink",
               "reward", "blink", "fact", "debt", "marble", "blink", "yak", "frightening", "suspend", "debt"]
combine = ''
sample_dict = {}
while sample_list:
    word = sample_list[0]
    if word not in sample_dict:
        count = sample_list.count(word)
        sample_dict[word] = count
        sample_list.pop(0)
    else:
        sample_list.pop(0)
        continue
for word, number in sample_dict.items():
    combine += int(number) * '*'
    print(f"{word} | {combine}")
    combine = ''




