import string
ALPHABET = list(string.ascii_uppercase)

def cipher(ciphertext,key):

    fullkey = ""
    while len(fullkey)<len(ciphertext):
        fullkey+=(key.translate(str.maketrans('', '', string.punctuation))).upper().replace(" ","")
    fullkey = fullkey[:len(ciphertext)]
    print(fullkey)

    plaintext = ""
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        if character.upper() in ALPHABET:
            position = ALPHABET.index(character.upper())
            newpos = position+ALPHABET.index(fullkey[i])
            plaintext+=ALPHABET[newpos%26]
        else:
            plaintext+=character
    return plaintext

print(cipher("Soylent Green is people.","spoiler"))