def spin_words(sentence):
    result = []
    
    word_list = sentence.split(' ')
    for word in word_list:
        if len(word) >= 5:
            reversed_word = word[::-1]
            result.append(reversed_word)
        else:
            result.append(word)
    
    
    return ' '.join(result)
print(spin_words("This sentence is a sentence"))