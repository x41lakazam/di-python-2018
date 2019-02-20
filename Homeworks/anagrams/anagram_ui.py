import string

import anagram_checker

checker = anagram_checker.AnagramChecker()

userword = input("Give me a word (type 'exit' to quit)")
userword = userword.strip()
userword = userword.lower()

while userword != "exit":
    if ' ' in userword:
        userword = input("Please input a single word (or 'exit')\n>>> ")
        continue

    for letter in userword:
        if letter not in string.ascii_lowercase:
            userword = input("Please input a real word (or 'exit')\n>>> ")
            continue

    # Word is valid
    # Check if the word is an english word
    english_flag    = checker.is_valid_word(userword)
    word_anagrams   = checker.get_anagram(userword)

    print("Your word: '{}'".format(userword))
    if english_flag:
        print("This is a valid english word.")
    else:
        print("This is not an english word...")
    print("Anagrams for your word:")
    for anagram in word_anagrams:
        print("- {}".format(anagram))
