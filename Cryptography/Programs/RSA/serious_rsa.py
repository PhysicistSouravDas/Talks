# Encryption/Decryption using this program cannot be broken without a key. 
# https://stuvel.eu/python-rsa-doc/usage.html

import rsa
from rsa.pkcs1 import decrypt

(pubKey, privKey) = rsa.newkeys(1024)
# print(pubKey)
# print(privKey)
message = "A very SECRET message."

ciphertext = rsa.encrypt(message.encode(), pubKey)
print("Cipher: \n{}".format(ciphertext))    # Shown in bytes

decrypt_cipher = rsa.decrypt(ciphertext, privKey)
print("The original message: \n{}".format(decrypt_cipher.decode()))