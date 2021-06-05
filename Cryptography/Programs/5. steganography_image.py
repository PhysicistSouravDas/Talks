from stegano import lsb     # least significant bit

secret = lsb.hide("./batman_trilogy_logo.png", "This is a very Secret Message!")
secret.save("./Steganographic_Image.png")