import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # String constants
chars = list(chars) #String -> List
key = chars.copy() # Copy the value for new object

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {key}")

# Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
       index = chars.index(letter)
       cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
       index = key.index(letter)
       plain_text += chars[index]

print(f"decrypted message: {plain_text}")
