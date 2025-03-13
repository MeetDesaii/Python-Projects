# Basic Ceaser Cipher Encryption and Decryption Concept!

import ListsData

letters_list = ListsData.small_letters
feature = ""
msg = ""
shift = 0

try:
    feature = input("Write 'encrypt' for Encryption or 'decrypt' for Decryption: ").lower()
    msg = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
except ValueError or NameError as e:
    print("Please enter the valid input!")
    exit()


def ceaser_cipher(msg_txt, shift_num, encrypt_or_decrypt):
    cipher_msg = ""
    for letter in msg_txt:
        if letter not in letters_list:
            cipher_msg += letter
        else:
            if encrypt_or_decrypt == "encrypt":
                shifted_position = letters_list.index(letter) + shift_num
            else:
                shifted_position = letters_list.index(letter) - shift_num
            # To avoid index out of bound error
            shifted_position %= len(letters_list)
            cipher_msg += letters_list[shifted_position]

    print(f"Cipher message: {cipher_msg}")


if feature == "encrypt" or feature == "decrypt":
    ceaser_cipher(msg_txt=msg, shift_num=shift, encrypt_or_decrypt=feature)
else:
    print("Please enter the valid input!")
