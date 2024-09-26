n = int(input())

for i in range(n):
    string_chars = input()
    offset = int(input())
    decrypted_string_chars = ''

    for char in string_chars:
        ordinal = ord(char) - offset
        if ordinal < ord('A'):
            ordinal = ord('Z') - (ord('A') - ordinal) + 1
        decrypted_string_chars += chr(ordinal)

    print(decrypted_string_chars)
