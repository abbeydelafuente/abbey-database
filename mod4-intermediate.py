# 1 Shift Letter
def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = alphabet.index(letter)
        shifted_index = (index + shift) % len(alphabet)
        return alphabet[shifted_index]
# test
# print(shift_letter([input letter here], [input value here])) 

# 2 Caesar Cipher
def caesar_cipher(message, shift):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_letters = {}
    for i in range(len(uppercase)):
        shifted_letters[uppercase[i]] = uppercase[(i + shift) % len(uppercase)]
    shifted_message = ""
    for uppercase in message:
        if uppercase == " ":
            shifted_message += " "
        else:
            shifted_message += shifted_letters[uppercase]
    return shifted_message
# test
# message = [input message here]
# shift = [input value here]
# encrypted_message = caesar_cipher(message, shift)
# print(encrypted_message) 

# 3 Shift by Letter
def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    letter_value = ord(letter) - ord("A")
    shift_value = ord(letter_shift) - ord("A")
    shifted_value = (letter_value + shift_value) % 26
    return chr(shifted_value + ord("A"))
# test
# print(shift_by_letter([input letter here], [input letter shift here]))

# 4 Vigenere Cipher
def vigenere_cipher(message, key):
    message = message.upper()
    key = key.upper()
    new_key = key
    while len(new_key) < len(message):
        new_key += key
    encrypted_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            encrypted_message += " "
        else:
            shift_value = ord(new_key[i]) - ord("A")
            shifted_letter = chr((ord(message[i]) - ord("A") + shift_value) % 26 + ord("A"))
            encrypted_message += shifted_letter
    return encrypted_message
# test
# print(vigenere_cipher([input message here], [input key here]))
