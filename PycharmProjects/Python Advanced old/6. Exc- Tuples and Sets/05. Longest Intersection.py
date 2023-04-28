def gen_sec(range_info):
    start, stop = [int(num) for num in range_info.split(',')]
    return set(range(start, stop + 1))


n = int(input())
max_list_set = set()
for _ in range(n):
    interval = input().split('-')
    set1 = gen_sec(interval[0])
    set2 = gen_sec(interval[1])
    set_intersect = set1.intersection(set2)
    length_set = len(set_intersect)
    if len(max_list_set) < len(set_intersect):
        max_list_set = set_intersect

print(f"Longest intersection is [{', '.join([str(num) for num in max_list_set])}] with length {len(max_list_set)}")