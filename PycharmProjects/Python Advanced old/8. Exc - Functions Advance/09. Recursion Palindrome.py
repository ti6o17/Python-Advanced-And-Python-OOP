def palindrome(word: str, index: int):

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    first_letter, last_letter = word[index], word[len(word) - index - 1]
    if first_letter != last_letter:
        return f"{word} is not a palindrome"

    index += 1
    return palindrome(word, index)


print(palindrome("peter", 0))