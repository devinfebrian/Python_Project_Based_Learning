import random
import string

# Using string module and random module

chars = " " + string.punctuation + string.digits + string.ascii_letters

# Added chars into a list so we can iterate
chars = list(chars)

# Copy the character into key variable and randomly shuffle everytime we run it.
key = chars.copy()
random.shuffle(key)

print(chars)
print(key)

# Input
plaintext = input("Enter text to encrypt: ")
ciphertext = ""

# Iterate every character from the input and map the key in that index and add it to the cipher text
for letter in plaintext:
  index = chars.index(letter)
  ciphertext += key[index]

print(f"Encrypted Message: {ciphertext}")

# Decryption function
encryptedtext = input("Enter Encrypted text: ")
decryptedtext = ""

# the same thing as previous for loop, but this time we mapped the index of the letter in the key
# and mapped it onto the original list of chars
for letter in encryptedtext:
  index = key.index(letter)
  decryptedtext += chars[index]

print(f"Decrypted Text: {decryptedtext}")