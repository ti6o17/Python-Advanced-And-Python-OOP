from collections import deque

que_vowels = deque(input().split())
que_consonants = deque(input().split())

word1 = "rose"
word2 = "tulip"
word3 = "lotus"
word4 = 'daffodil'

flag = False
word = ''
while que_consonants and que_vowels:
    vowel = que_vowels.popleft()
    consonant = que_consonants.pop()
    if vowel in word1:
        word1 = word1.replace(vowel, "")
    if consonant in word1:
        word1 = word1.replace(consonant, "")

    if vowel in word2:
        word2 = word2.replace(vowel, "")
    if consonant in word2:
        word2 = word2.replace(consonant, "")

    if vowel in word3:
        word3 = word3.replace(vowel, "")
    if consonant in word3:
        word3 = word3.replace(consonant, "")

    if vowel in word4:
        word4 = word4.replace(vowel, "")
    if consonant in word4:
        word4 = word4.replace(consonant, "")

    if not word1:
        word = "rose"
        flag = True
        break
    if not word2:
        word = "tulip"
        flag = True
        break
    if not word3:
        word = "lotus"
        flag = True
        break
    if not word4:
        word = "daffodil"
        flag = True
        break

if not flag:
    print("Cannot find any word!")
    if que_vowels:
        print(f"Vowels left: {' '.join(que_vowels)}")
    if que_consonants:
        print(f"Consonants left: {' '.join(que_consonants)}")
else:
    print(f"Word found: {word}")
    if que_vowels:
        print(f"Vowels left: {' '.join(que_vowels)}")
    if que_consonants:
        print(f"Consonants left: {' '.join(que_consonants)}")
