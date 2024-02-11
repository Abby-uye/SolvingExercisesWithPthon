def character_frequency(word):
    word_dictionary = {}
    for letters in word:
        word_count = 0
        for letter in word:
            if letters == letter:
                word_count += 1
        word_dictionary[letters] = [word_count]
    return word_dictionary


theWord = "semicolon.africa"
newDictionary = character_frequency(theWord)
print(newDictionary)
