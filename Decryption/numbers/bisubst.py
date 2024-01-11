def load_bigram_key(file_path):
    """ Load bigram key from a file. """
    key = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                key[parts[0]] = parts[1]
    return key

def encrypt_bigram(key):
    """ Encrypt text using a bigram key. """
    encrypted = ""
    with open("big.txt","r") as file:
        text = file.read()
    text = text.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    if len(text) % 2 != 0:
        text += 'X'  # Padding if necessary

    for i in range(0, len(text), 2):
        bigram = text[i:i+2]
        encrypted += key.get(bigram, "**")  # Use bigram from key or original if not found

    return encrypted

# Path to the key file
key_file = 'bigram_key.txt'

# Load the key
bigram_key = load_bigram_key(key_file)

# Example text
plaintext = "HELLO WORLD"

# Encrypt the text
ciphertext = encrypt_bigram(bigram_key)
print("Done")
with open('decrypt.txt', 'w') as file:
    file.write(ciphertext)