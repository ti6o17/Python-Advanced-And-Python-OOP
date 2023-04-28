from collections import deque

main_colors = {"red", "blue", "yellow"}
second_colors = {"orange", "purple", "green"}
substring = deque(input().split())
collected_colors = deque()

while substring:
    first_substr = substring.popleft()
    second_substr = substring.pop() if substring else ''

    result = first_substr + second_substr
    if result in main_colors or result in second_colors:
        collected_colors.append(result)
        continue
    result = second_substr + first_substr
    if result in main_colors or result in second_colors:
        collected_colors.append(result)
        continue

    first_substr = first_substr[:-1]
    second_substr = second_substr[:-1]

    if first_substr :
        substring.insert(len(substring) // 2, first_substr)

    if second_substr:
        substring.insert(len(substring) // 2, second_substr)

dict_second_main_colors = {
    "orange": ["red", "yellow"],
    "purple": ["blue", "red"],
    "green": ["blue", "yellow"]
}

flag = False
if "orange" in collected_colors or "purple" in collected_colors or "green" in collected_colors:
    if "orange" in collected_colors and set(dict_second_main_colors["orange"]).issubset(set(collected_colors)):
        print(list(collected_colors))
    elif "purple" in collected_colors and set(dict_second_main_colors["purple"]).issubset(collected_colors):
        print(list(collected_colors))
    elif "green" in collected_colors and set(dict_second_main_colors["green"]).issubset(collected_colors):
        print(list(collected_colors))

    elif "orange" in collected_colors:
        collected_colors.remove("orange")
        print(list(collected_colors))
    elif "purple" in collected_colors:
        collected_colors.remove("purple")
        print(list(collected_colors))
    elif "green" in collected_colors:
        collected_colors.remove("green")
        print(list(collected_colors))
else:
    print(list(collected_colors))
