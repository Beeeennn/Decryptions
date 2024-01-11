import numpy as np
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def singles(f):
    text = f.read()
    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(len(text))
    total = 0
    letterdict = {}
    hold = 0
    for i in range(len(text)):
        if text[i].upper() in Alphabet:
            num = Alphabet.index(str(text[i]).upper())
            freq[num] += 1
            total += 1
    for i in range(len(Alphabet)):
        hold += freq[i]
        letterdict[Alphabet[i]] = ((freq[i]*100000)//total)/1000
    findict = list(reversed(sorted(letterdict.items(), key=lambda item: item[1])))
    return findict



def pairs(f):
    freqdub = np.zeros(shape = (26,26))
    dubdict = {}
    text = f.read()
    #print(text)
    total = 0
    for i in range(len(text)-1):
        if text[i].upper() in Alphabet and text[i+1].upper() in Alphabet:
            num1 = Alphabet.index(str(text[i]).upper())
            num2 = Alphabet.index(str(text[i+1]).upper())
            freqdub[num1][num2]+= 1
            total += 1
    perc = 0
    for i in range(len(Alphabet)):
        for j in range(len(Alphabet)):
            if ((freqdub[i][j]*100000)//total)/1000 > 0.1:
                dubdict[Alphabet[i]+Alphabet[j]]= ((freqdub[i][j]*100000)//total)/1000
    findict = list(reversed(sorted(dubdict.items(), key=lambda item: item[1])))
    return findict



def tripples(f):
    tripdict = {}
    freqtrip = np.zeros(shape=(26,26,26))

    text = f.read()
    #print(text)
    total = 0
    for i in range(len(text)-2):
        if text[i].upper() in Alphabet and text[i+1].upper() in Alphabet and text[i+2].upper() in Alphabet:
            num1 = Alphabet.index(str(text[i]).upper())
            num2 = Alphabet.index(str(text[i+1]).upper())
            num3 = Alphabet.index(str(text[i+2]).upper())
            freqtrip[num1][num2][num3] += 1
            total += 1
    perc = 0
    for i in range(len(Alphabet)):
        for j in range(len(Alphabet)):
            for k in range(len(Alphabet)):
                if ((freqtrip[i][j][k]*100000)//total)/1000 > 0.1:
                    tripdict[Alphabet[i]+Alphabet[j]+Alphabet[k]] = ((freqtrip[i][j][k]*100000)//total)/1000
                    
    findict = list(reversed(sorted(tripdict.items(), key=lambda item: item[1])))
    return findict


def quads(f):
    quaddict = {}
    freqtrip = np.zeros(shape=(26,26,26,26))

    text = f.read()
    #print(text)
    total = 0
    for i in range(len(text)-3):
        if text[i].upper() in Alphabet and text[i+1].upper() in Alphabet and text[i+2].upper() in Alphabet and text[i+3].upper() in Alphabet:
            num1 = Alphabet.index(str(text[i]).upper())
            num2 = Alphabet.index(str(text[i+1]).upper())
            num3 = Alphabet.index(str(text[i+2]).upper())
            num4 = Alphabet.index(str(text[i+3]).upper())
            freqtrip[num1][num2][num3][num4] += 1
            total += 1
    perc = 0
    for i in range(len(Alphabet)):
        for j in range(len(Alphabet)):
            for k in range(len(Alphabet)):
                for l in range(len(Alphabet)):
                    if ((freqtrip[i][j][k][l]*100000)//total)/1000 > 0.1:
                        quaddict[Alphabet[i]+Alphabet[j]+Alphabet[k]+Alphabet[l]] = ((freqtrip[i][j][k][l]*1000000)//total)/10000
    findict = list(reversed(sorted(quaddict.items(), key=lambda item: item[1])))
    return findict

def finddiff(dict1,dict2):
    totaldiff = 0
    overall = 0
    for i in range(min(len(dict1),len(dict2))):
        totaldiff += ((list(dict1)[i][1]) - (list(dict2)[i][1]))**2
        overall += totaldiff**0.5
    return overall

def optimise(dict1,dict2):
    pass

f = open("count.txt", "r", encoding="utf-8")
freq2 = pairs(f)
f.close()

f2 = open("count2.txt","r", encoding="utf-8")
freq = pairs(f2)
print(f2.read())
print(singles(f2))


"""
Line up the letters so I will need to do trial decryptions with the encrypted text and compare it to the ones at the top, lining up by pairs of characters
rather than order, lining up as many as possible with the ones at the top would be a good start, then refine by swapping using the single character probabilites,
checking difference against double each time for lowest difference, if changing makes minimal positive difference, move to lower probability ones

will need a dictionary in the format of {enrypted letter : letter attempt}, then convert the encryptions in the dictionary to the new one (might be easier
to make a new set of functions to add to a new character dictionary, or even modify the old ones) then recheck, find difference, if it is lower keep the higher letters
and move to the lower ones (probably letters should not be more than 5 away from frequency position)



"""