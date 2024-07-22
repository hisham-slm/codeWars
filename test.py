alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
counter = 0
text = 'rovwsoiv'
key_length = len(key)
new_key = ''
result = []
cipher_sets = {}


# for i in range(26):
#     cipher_sets.update({alphabet[i] : alphabet[i:] + alphabet[:i]})

# if key_length != len(text):
#     for _ in enumerate(text, 1):
#         new_key += key[counter]
#         counter += 1
#         if counter == key_length:
#             counter = 0
# else:
#     new_key = key
# for letter_k, letter_c in zip(new_key, text):
#     result.append(alphabet[cipher_sets[letter_k].index(letter_c)])
    
# print(result)


print(key.upper() == True)