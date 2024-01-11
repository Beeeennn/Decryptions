with open("encrypted.txt", 'r') as file:
    content = file.read()
i = 1
ends =  ""
for char in content:
    ends += char
    if i%2 == 0:
        ends += " "
    i += 1
with open('big.txt', 'w') as file:
    file.write(ends)