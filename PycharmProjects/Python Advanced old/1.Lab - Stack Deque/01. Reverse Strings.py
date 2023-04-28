
text_to_revert = input()
list_text_to_revert = []
for letter in text_to_revert:
    list_text_to_revert.append(letter)
for _ in range(len(list_text_to_revert)):
    letter2 = list_text_to_revert.pop(-1)

    print(letter2, end='')