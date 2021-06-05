import string
alphabet = string.ascii_lowercase       # abcdefghijklmnopqrstuvwxyz
alphabet_list = list(alphabet)          # list of letters of alphabet

letter = str(input("Enter letter to be shifted: "))
shift = int(input("Enter amount of shift (-ve allowed): "))

letter_pos = alphabet_list.index(letter)
if letter_pos + shift >= 26:
    shift -= 26
print("Output: ", alphabet_list[shift + letter_pos])
