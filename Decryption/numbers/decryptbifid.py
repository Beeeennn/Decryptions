import itertools
import string
from collections import Counter
import nltk
from nltk.corpus import words

# Install word list
nltk.download('words')
def read_ciphertext(file_path):
    """Read ciphertext from a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_to_file(output, file_path):
    """Write the output to a file."""
    with open(file_path, 'w') as file:
        file.writelines(output)

def generate_key_square(key, alphabet):
    key_square = ''.join(sorted(set(key), key=key.index))
    key_square += ''.join(c for c in alphabet if c not in key_square)
    key_square_matrix = [list(row) for row in zip(*[iter(key_square)]*5)]
    return key_square_matrix



def decrypt_bifid(ciphertext, key_square):
    """Decrypt a ciphertext using a Bifid cipher with a given key square."""
    # Flatten the key square for easier lookup
    flat_key_square = sum(key_square, [])

    # Create a dictionary to map each character to its row and column in the key square
    char_to_pos = {char: (i // 5, i % 5) for i, char in enumerate(flat_key_square)}

    # Convert each character in the ciphertext to its corresponding row and column
    rows_and_cols = [char_to_pos[char] for char in ciphertext]

    # Split the rows and columns
    rows, cols = zip(*rows_and_cols)

    # Interweave the rows and columns
    combined = sum(zip(rows, cols), ())

    # Split the combined list in half to get the new rows and columns
    split_index = len(combined) // 2
    new_rows, new_cols = combined[:split_index], combined[split_index:]

    # Convert the new row and column pairs back to characters
    decrypted_text = ''.join(flat_key_square[row * 5 + col] for row, col in zip(new_rows, new_cols))

    return decrypted_text


def score_text(text):
    """Score decrypted text based on character and bigram frequency."""
    char_frequency = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28,
                      'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,
                      'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11,
                      'K': 0.69, 'X': 0.17, 'Q': 0.11, 'Z': 0.07}
    bigram_frequency = {'TH': 2.71, 'EN': 1.13, 'NG': 0.89, 'HE': 2.33, 'AT': 1.12, 'AL': 0.88,
                        'IN': 2.03, 'ED': 1.08, 'IT': 0.88, 'ER': 1.78, 'ND': 1.07, 'AS': 0.87,
                        'AN': 1.61, 'TO': 1.07, 'IS': 0.86, 'RE': 1.41, 'OR': 1.06, 'HA': 0.83,
                        'ES': 1.32, 'EA': 1.00, 'ET': 0.76}
    
    score = 0
    for char in text:
        score += char_frequency.get(char.upper(), 0)
    for i in range(len(text)-1):
        bigram = text[i:i+2].upper()
        score += bigram_frequency.get(bigram, 0)
    return score

def brute_force_bifid(ciphertext, alphabet):
    outcomes = []
    english_words = set(words.words())
    
    for key_length in range(7, 8):
        for key in itertools.product(alphabet, repeat=key_length):
            key = ''.join(key)
            # Check if the key is an English word
            if key.lower() in english_words:
                print(key)
                key_square = generate_key_square(key, alphabet)
                decrypted_text = decrypt_bifid(ciphertext, key_square)
                score = score_text(decrypted_text)
                outcomes.append((score, key, decrypted_text[:100]))
    
    return sorted(outcomes, key=lambda x: x[0], reverse=True)[:20]


# Define the 25-letter alphabet (excluding 'J')
alphabet = string.ascii_uppercase.replace('J', '')

# Read the ciphertext from 'encrypted.txt'
ciphertext = read_ciphertext('encrypted.txt')
ciphertext = ''.join(c for c in ciphertext.upper() if c in alphabet)

# Brute force the Bifid cipher and get likely outcomes
top_outcomes = brute_force_bifid(ciphertext, alphabet)

# Write the top 20 outcomes to 'out.txt'
output = [f"Key: {key}, Decrypted Text (First 100 chars): {text}\n" for _, key, text in top_outcomes]
write_to_file(output, 'out.txt')

# Indicating that the script is complete
print("Script executed successfully. Results written to 'out.txt'.")