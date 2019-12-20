# O(n) time | O(n) space 

# in unicode, a = 97 and z = 122

def caesar_cipher(string, key):
    newLetters = []
    newKey = key % 26 # number of letters in alphabet
    for letter in string:
        newLetters.append(get_new_letter(letter, newKey))
    return "".join(newLetters)

def get_new_letter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + (newLetterCode % 122))


print(caesar_cipher("abby", 235))