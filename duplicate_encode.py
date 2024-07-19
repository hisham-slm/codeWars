def duplicate_encode(word):
    result = []
    char_counter = {}
    word.lower()
    print(word)
    
    for char in word:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    
    for char in word:
        if char_counter[char] >= 2:
            result.append(')')
        else:
            result.append('(')
    print(char_counter)
    return "".join(result)
print(duplicate_encode("Success"))