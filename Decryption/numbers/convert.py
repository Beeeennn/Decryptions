def convert_string_to_alphabetical_numbers(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Convert each character to its alphabetical number
    alphabetical_numbers = []
    for char in content.upper():
        if char.isalpha():
            number = ord(char) - ord('A') + 1
            alphabetical_numbers.append(str(number))

    # Join the numbers into a string
    result = ' '.join(alphabetical_numbers)
    return result

out = convert_string_to_alphabetical_numbers('text.txt')
with open('num.txt', 'w') as file:
    file.write(out)
