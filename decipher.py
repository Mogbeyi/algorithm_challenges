def decipher(ciphertext, known_word):
    for shift in range(26):
        plaintext = ""
        
        for char in ciphertext:
            if char.islower():
                position = ord(char) - ord('a')
                new_position = (position + shift) % 26
                plaintext += chr(new_position + ord('a'))
            elif char.isupper():
                position = ord(char) - ord('A')
                new_position = (position + shift) % 26
                plaintext += chr(new_position + ord('A'))
            else:
                plaintext += char
                
        if known_word in plaintext:
            return (plaintext)
            
print(decipher("Eqfkpi vguvu ctg hwp cpf ejcnngpikpi", "fun"))
print(decipher("hello", "jgnnq"))

