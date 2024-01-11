def read_square(file_name):
    """
    Reads a 5x5 square from a file.
    Each line in the file represents a row in the square.
    """
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def decrypt_bigram(bigram, square1, square2, square3, square4):
    """
    Decrypts a bigram using the four squares.
    Returns '**' if the bigram cannot be decrypted due to unknown letters in the keys.
    """
    # Finding positions in square1 and square4
    for i in range(5):
        for j in range(5):
            if square1[i][j] == bigram[0]:
                row1, col1 = i, j
            if square4[i][j] == bigram[1]:
                row4, col4 = i, j
    
    # Decrypting using square2 and square3
    try:
        decrypted_bigram = square2[row1][col4] + square3[row4][col1]
        return decrypted_bigram
    except UnboundLocalError:  # One or more characters in the bigram were not found
        return '**'

def decrypt_message(encrypted_text, key1, key2):
    """
    Decrypts an encrypted message using two key squares and the Four-Square cipher.
    """
    # Standard square (A-Z, excluding J)
    standard_square = [ "ABCDE", "FGHIK", "LMNOP", "QRSTU", "VWXYZ" ]

    # Reading key squares
    square1 = read_square(key1)
    square2 = standard_square
    square3 = standard_square
    square4 = read_square(key2)

    print(square1)
    # Decrypting bigrams
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        bigram = encrypted_text[i:i+2]
        decrypted_text += decrypt_bigram(bigram, square1, square2, square3, square4)

    return decrypted_text

# Example usage (commented out as we don't have actual files in this environment)
encrypted_text = open("encrypted.txt", "r").read().replace("\n", "").upper()
decrypted_text = decrypt_message(encrypted_text, "key1.txt", "key2.txt")
with open("decrypted_message.txt", "w") as file:
    file.write(decrypted_text)
