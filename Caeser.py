import string
direction = input("Type 'encode' to encrypt and Type 'decode' to decrypt: \n").lower()
user_text = input("Enter original_text: ")
user_amount = int(input("Enter shift_amounts: "))


#To  create a function called encrypt() that takes original_text and shift_amounts as 2 inputs

def encrypt(original_text, shift_amounts):
    alphabet = string.ascii_lowercase
#Translation table
    shifted_alphabet = alphabet[shift_amounts % 26:] + alphabet[:shift_amounts % 26]
    table = str.maketrans(alphabet, shifted_alphabet)
    return original_text.translate(table)

print(encrypt(original_text = user_text, shift_amounts = user_amount))

def decrypt(original_text, shift_amounts):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift_amounts % 26:] - alphabet[:shift_amounts % 26]
    shifted_alphabet = alphabet[:shift_amounts % 26] + alphabet[shift_amounts % 26:]
    table = str.maketrans(alphabet, shifted_alphabet)
    return original_text.translate(table)
print(decrypt(original_text = user_text, shift_amounts = user_amount))


