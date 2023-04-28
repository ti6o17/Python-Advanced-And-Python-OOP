n, m = input().split()
n = int(n)
m = int(m)
nums1 = []
nums2 = []
for _ in range(n):
    nums1.append(int(input()))
for _ in range(m):
    nums2.append(int(input()))
z = set(nums1).intersection(set(nums2))
z = list(z)

for num in z:
    print(num)
