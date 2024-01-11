Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

f = open("count2.txt", "r", encoding="utf-8")
text = f.read()
f.close()

#print(text)
total = 0
for i in range(len(text)):
    if text[i] in Alphabet:
        num = Alphabet.index(str(text[i]).upper())
        freq[num] += 1
        total += 1
perc = 0
for i in range(len(Alphabet)):
    print(Alphabet[i]+" : "+str((freq[i]*100)//total))
    perc += (freq[i]*100)//total
print(perc)