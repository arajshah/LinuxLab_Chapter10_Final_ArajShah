def encryptor(text):
    text = "".join(text.split()).upper()
    small = ""
    big = ""
    encrypted = ""
    for i, j in enumerate(text):
        small = small + chr(ord(j) + 1)
        if len(small) == 5:
            big = big + small + " "
            small = ""
        if len(big.split()) == 10:
            encrypted = encrypted + big + "\n"
            big = ""
            
    return encrypted + big + small 

        
