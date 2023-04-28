def words_sorting(*args):
    sum = 0
    sum_items = 0
    dict_word = {}
    list_words = []
    for word in args:
        sum = 0
        for letter in word:
            sum += ord(letter)
        dict_word[word] = sum
    for item in dict_word:
        sum_items += dict_word.get(item)
    if sum_items % 2 == 0:
        sorted_dict_word = sorted(dict_word.items(), key=lambda x: (x[0]))
    elif sum_items % 2 == 1:
        sorted_dict_word = sorted(dict_word.items(), key=lambda x: (-x[1]))
    for key, item in sorted_dict_word:
        list_words.append(f"{key} - {item}")
    return '\n'.join(list_words)


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

