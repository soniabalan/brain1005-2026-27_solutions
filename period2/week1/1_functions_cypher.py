# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:11:05 2026

@author: Sonia
"""
def encrypt(text, shift = 3):
    text = text.upper()  # .upper() transforms the string into an uppercase
  
    # initialise empty string to store the hidden message
    message = ""

    # create [alphabet] to index through
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # loop over each letter in the code
    for letter in text: 
        if letter in alphabet:
            # find letter index
            letter_ix = int(alphabet.index(letter))
            # shift indes
            letter_msg_ix = letter_ix + shift
            letter_msg_ix = letter_msg_ix % len(alphabet)
            
            # add letter to message
            message = message + alphabet[letter_msg_ix]
        else:
            message = message + letter
    
    # output the hidden message
    print(f"the encrypted message is: {message}")
    return message

def decrypt(text, shift = 3):
    return encrypt(text, shift=-shift)

encrypt("BRAIN!")
encrypt("xyz!", 3)
encrypt("Brain 1005!")
encrypt("", 3)

decrypt("EUDLQ", 3)
decrypt(encrypt("HELLO!", 5), 5)

