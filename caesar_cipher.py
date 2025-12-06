def caesar(text,shift, encrypt=True):
  # Shift condition for out of range value
  if shift < 1 or shift > 25:
    print("Shift must be between 1-25")


  # Shift condition if value entered is not an integer value
  if not isinstance(shift, int):
    print("Shift must be an integer value.")

  # Text Condition if value entered is not an string
  if not isinstance(text, str):
    print("Text must not contain number or special character")

  # This will unshift the alphabet if encrypt value is False
  if not encrypt:
    shift = -shift
 
  # We will be subtituting alphabet using shift value
  # for instance if shift value is 3 then the start of the alphabet is d and a,b,c is shifted into the end of the alphabet
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]

  translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
  return text.translate(translation_table)

# Encryption Function taking text and shift value as parameter
def encrypt(text,shift):
  return caesar(text,shift, encrypt=True)

def decrypt(text,shift):
  return caesar(text,shift, encrypt=False)

def main():
  plaintext = input("Enter Word: ")
  shifting = int(input("Enter Shift Value 1-25: "))

  # Performing encryption taking input from user
  ciphertext = encrypt(plaintext, shifting)
  print(ciphertext)

  # Decrypt the message
  ciphertext = input("Enter Encrypted Words: ")
  decryptedtext = decrypt(ciphertext, shifting)
  print(decryptedtext)

main()
