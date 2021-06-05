import hashlib      # python standard library

password = "P@S$w0rd"

bytes_password = password.encode()      # converting plaintext to bytes
hash = hashlib.sha256(bytes_password)   # outputs a hash in bytes
# instead of sha256(), you can use sha1(), sha224(), sha384(), sha512(),
# sha3_224(), sha3_256(), sha3_384(), sha3_512()

hash_digest = hash.hexdigest()          # outputs in hexadecimal
print(hash_digest)                      # outputs a 256 bit (256/4 = 64 character) hash