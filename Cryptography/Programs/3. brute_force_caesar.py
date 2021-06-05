# Using OOP paradigm here
import string

class Cipher():
    alphabet = string.ascii_lowercase

    def __init__(self, file_name=None):
        self.file_name = file_name

    def read_cipher(self):
        f = open(self.file_name, "r")
        cipher_text = f.read()
        return cipher_text.lower()

    def decrypt_cipher(self):
        results = ""
        for shift in range(len(Cipher.alphabet)):
            pure = ""
            for letter in self.read_cipher():
                mod_shift = shift
                if ord(letter) + mod_shift > 122:
                    mod_shift -= 26
                # print('shift', shift)
                num = ord(letter) + mod_shift
                # print('num', num)
                pure += chr(num)
            results = results + pure + "\n\n"
        return results

cipher1 = Cipher('caesar_cipher.txt')
print(cipher1.read_cipher())
print(cipher1.decrypt_cipher())