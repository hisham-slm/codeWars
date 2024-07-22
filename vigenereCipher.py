class VigenereCipher(object):
    def __init__(self, key, alphabet) -> None:
        self.key = key
        self.alphabet = alphabet
        self.cipher_sets = {}
        self.counter = 0
        self.key_length =  len(key)
        self.len_alphabet = len(alphabet)

        for i in range(self.len_alphabet):
            self.cipher_sets.update({self.alphabet[i] : self.alphabet[i:] + self.alphabet[:i]})
    def encode(self, text):
        alphabet = self.alphabet
        key = self.key
        new_key = ''
        cipher_sets = self.cipher_sets
        counter = self.counter
        key_length = self.key_length
        result = []
        
        if key_length != len(text):
            for _ in enumerate(text, 1):
                new_key += key[counter]
                counter += 1
                if counter == key_length:
                    counter = 0
        else:
            new_key = key

        for letter_t, letter_k in zip(text, new_key):
            try:
                result.append(cipher_sets[str(letter_t)][alphabet.index(letter_k)])
            except:
                result.append(letter_t)
        return ''.join(result)
    
    def decode(self, text):
        alphabet = self.alphabet
        key = self.key
        cipher_sets = self.cipher_sets
        counter = self.counter
        text = text
        key_length = self.key_length
        result = []
        new_key = ''
        
        if key_length != len(text):
            for _ in enumerate(text, 1):
                new_key += key[counter]
                counter += 1
                if counter == key_length:
                    counter = 0
        else:
            new_key = key
            
        for letter_k, letter_t in zip(new_key, text):
            try:
                result.append(alphabet[cipher_sets[letter_k].index(letter_t)])
            except:
                result.append(letter_t)

        return ''.join(result)
    
abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
print(VigenereCipher(key, abc).encode(text='codewars'))
print(VigenereCipher(key, abc).decode(text='CODEWARS'))