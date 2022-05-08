import sys
import string

SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "ENCODE":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(LETTER) + SHIFT
            ENCODED = ENCODED + LETTERS[x]
if CHOICE == "DECODE":
    for LETTER in WORD:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(LETTER) - SHIFT
            ENCODED = ENCODED + LETTERS[x]

print(ENCODED)
sys.exit()
