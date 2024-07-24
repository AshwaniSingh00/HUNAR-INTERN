def encrypt(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift +3) % 26 + shift)
        else:
            encrypted += char
    return encrypted
def decrypt(encrpted_text):
    decrypted = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - shift- 3) % 26 + shift)
        else:
            decrypted += char
    return decrypted

# Example usage:
text = input("Enter the string for encryption: ")

encrypted_text = encrypt(text)
decrypted_text = decrypt(encrypted_text)

print("Plaintext:",text)
print("Encrypted:",encrypted_text)
print("Decrypted: ",decrypted_text)
