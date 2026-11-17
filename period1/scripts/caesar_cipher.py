"""
Caesar Cipher

Created on Tue Sep 22 11:06:43 2026

@author: Sonia Balan
"""

# get the coded message and shift from user
code = input("type the message that you want to decode: ").upper().strip() 
    # .upper() transforms the string into an uppercase
    # .strip() removes trailing spaces if accidentally added by user
shift = int(input("what is the shift (integer): "))

# initialise empty string to store the hidden message
message = ""

# create [alphabet] to index through
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# loop over each letter in the code
for letter in code: 
    letter_ix = int(alphabet.index(letter))
    # shift the letter index
    letter_msg_ix = letter_ix - shift
    # if index is out of bounds, reset index
    # print(f"letter: {letter}, ix: {letter_ix}, ix-shift :{letter_msg_ix}")
    if letter_msg_ix > len(alphabet)-1: # to beginning of the alphabet
        letter_msg_ix = letter_msg_ix - len(alphabet)
    elif letter_msg_ix < 0: # to the back of the alphabet
        letter_msg_ix = len(alphabet) + letter_msg_ix
        
    # nice smart alternative
    # letter_msg_ix = letter_msg_ix % len(alphabet)
    
    # add letter to message
    message = message + alphabet[letter_msg_ix]

# output the hidden message
print(f"the code says: {message}")