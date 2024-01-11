Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Cypher   = ["E","N","O","F","D","P","Q","B","R","S","T","U","V","W","X","Y","*","C","G","A","H","I","J","K","L","M"]
ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

f = open("encrypted.txt", "r", encoding="utf-8")
text = f.read()
f.close()

#print(text)

plain = ""
for character in text:
    if character.upper() in Alphabet:
        num = Alphabet.index(character.upper())
        plain += Cypher[num]
    else:
        plain += character

print(plain)

f = open("plaintext.txt", "w", encoding="utf-8")
f.write(plain)
f.close()