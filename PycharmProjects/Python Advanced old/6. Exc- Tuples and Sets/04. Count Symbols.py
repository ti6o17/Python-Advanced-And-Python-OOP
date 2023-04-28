letters = input()
list_letters = []
dict_letters = dict()
for letter in letters:
    list_letters.append(letter)
list_letters = sorted(list_letters)
for letter_count in list_letters:
    counted_letter = list_letters.count(letter_count)
    if not letter_count in dict_letters:
        dict_letters[letter_count] = counted_letter
# print(dict_letters)
for number, letter in dict_letters.items():
    print(f"{number}: {letter} time/s")
