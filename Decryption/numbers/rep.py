def replace(text,keep):
    new = ""
    for character in text:
        if character in keep:
            new += character
        else:
             new += "*"
    return new

def oddreplace(text,keep):
    new = ""
    next = False
    for character in text:
        if character in keep:
            new += character
            next = True
        else:
            if next:
                new += character
                next = False
            else:
                new += "*"
    return new



with open("encrypted.txt","r") as file:
        text = file.read()
newt = oddreplace(text,["A"])
with open('replaced.txt', 'w') as file:
    file.write(newt)
