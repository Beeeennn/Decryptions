import itertools

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace('\n', '').replace(' ', '')

def create_grid(text, rows):
    columns = len(text) // rows
    return [text[i * columns:(i + 1) * columns] for i in range(rows)]

def decrypt(grid):
    columns = len(grid[0])
    decrypted_text = ''
    for col in range(columns):
        for row in grid:
            if col < len(row):
                decrypted_text += row[col]
    return decrypted_text

def score_text(text):
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
    score = 0
    for word in common_words:
        score += text.count(word)
    return score

def brute_force_decrypt(text):
    results = []
    for rows in range(1, min(11, len(text) + 1)):
        grid = create_grid(text, rows)

        for perm in itertools.permutations(range(rows)):
            permuted_grid = [grid[i] for i in perm]
            decrypted_text = decrypt(permuted_grid)
            score = score_text(decrypted_text)
            results.append((score, rows, perm, decrypted_text))

    return sorted(results, reverse=True)[:10]

def main():
    file_path = 'codedmsg.txt'  # Replace with your file path
    text = read_file(file_path)
    top_results = brute_force_decrypt(text)

    for result in top_results:
        score, rows, perm, decrypted_text = result
        print(f'Score: {score}, Rows: {rows}, Permutation: {perm}, Decrypted: {decrypted_text}')

if __name__ == '__main__':
    print("Starting")
    main()