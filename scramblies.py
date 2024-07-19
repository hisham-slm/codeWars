def letter_counter(word):
    counter = {}
    for letter in word:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return {key: counter[key] for key in sorted(counter)}
 

       
def scramble(s1, s2):
    result = []
    word1 = letter_counter(s1)
    word2 = letter_counter(s2)
    for letter in word2.keys():
       if letter in word1.keys():
           if word2[letter] <= word1[letter]:
               result.append(True)
           else:
               result.append(False)
       else:
           return False
    return all(result)

print(scramble('scriptingjava', 'javascript'))