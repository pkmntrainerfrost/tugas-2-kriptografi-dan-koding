# 18221102 | Salman Ma'arif Achsien
# 18221

import base64

# Fungsi untuk menghilangkan karakter selain spasi + mengubah kapitalisasi

def preprocess(string:str):

    preprocessed_string = ""

    for char in string:

        if char.isalpha():
            preprocessed_string += char.upper()

    return preprocessed_string

# Fungsi-fungsi untuk mengubah output ke base64 / mengubah input base64 ke ASCII

def base64Encrypt(string:str):

    plaintext_bytes = string.encode("ascii")

    base64_bytes = base64.b64encode(plaintext_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string

def base64Decrypt(string:str):

    base64_bytes = string.encode("ascii")

    plaintext_bytes = base64.b64decode(base64_bytes)
    plaintext_string = plaintext_bytes.decode("ascii")

    return plaintext_string

# Fungsi-fungsi standard vigenere cipher

def vigenereEncrypt(plaintext:str, key:str):

    plaintext_preprocessed = preprocess(plaintext)
    key_preprocessed = preprocess(key)

    ciphertext = ""
    i = 0

    for char in plaintext_preprocessed:

        ciphertext += chr(((ord(char) + ord(key_preprocessed[i])) % 26) + ord("A"))

        i = (i + 1) % (len(key_preprocessed))

    return ciphertext

def vigenereDecrypt(ciphertext:str, key:str):

    ciphertext_preprocessed = preprocess(ciphertext)
    key_preprocessed = preprocess(key)

    plaintext = ""
    i = 0

    for char in ciphertext_preprocessed:

        plaintext += chr(((ord(char) - ord(key_preprocessed[i])) % 26) + ord("A"))

        i = (i + 1) % (len(key_preprocessed))

    return plaintext

# Fungsi-fungsi extended vigenere cipher (WIP)

# Fungsi-fungsi playfair cipher

def playfairGenerateKeyMatrix(key:str):

    key_matrix = [["" for i in range(5)] for j in range(5)]
    key_preprocessed = "".join(dict.fromkeys(preprocess(key).replace("J","")))

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    i, j = 0, 0
    for char in key_preprocessed:

        key_matrix[i][j] = char

        j += 1

        if j >= 5:
            j = 0
            i += 1
        
        alphabet = alphabet.replace(char,"")

    for char in alphabet:

        key_matrix[i][j] = char

        j += 1

        if j >= 5:
            j = 0
            i += 1

    return key_matrix

def encryptPlayfair(plaintext:str, key:str):
    
    key_matrix = playfairGenerateKeyMatrix(key)
    plaintext_preprocessed = preprocess(plaintext).replace("J","I")

    plaintext_padded = ""
    second_letter = 0

    for char in plaintext_preprocessed:

        if not second_letter:
            plaintext_padded += char
            second_letter = True

        else:
            if plaintext_padded[-1] == char:
                plaintext_padded += ("X " if plaintext_padded[-1] != "X " else "Z ")
                plaintext_padded += char
            else:
                plaintext_padded += char + " "
                second_letter = False

    if second_letter:
        plaintext_padded += "X"

    bigrams = plaintext_padded.split(" ")
    ciphertext = ""

# Fungsi-fungsi product cipher

def encryptProductCipher(plaintext:str, vigenere_key:str, transposition_key:int):

    vigenere_ciphertext = vigenereEncrypt(plaintext,vigenere_key)

    transposition_matrix = [["" for i in range(transposition_key)] for i in range(-(len(vigenere_ciphertext) // -transposition_key))]
    ciphertext = ""

    i, j = 0, 0
    for char in vigenere_ciphertext:

        transposition_matrix[i][j] = char

        j += 1

        if j >= transposition_key:
            j = 0
            i += 1

    for j in range(j,transposition_key):

        transposition_matrix[i][j] = "X"

    for j in range(transposition_key):

        for i in range(len(transposition_matrix)):

            ciphertext += transposition_matrix[i][j]

    return ciphertext

def decryptProductCipher(ciphertext:str, vigenere_key:str, transposition_key:int):

    vigenere_plaintext = vigenereDecrypt(ciphertext,vigenere_key)

    transposition_matrix = [["" for i in range(-(len(vigenere_plaintext) // -transposition_key))] for i in range(transposition_key)]
    plaintext = ""

    i, j = 0, 0
    for char in vigenere_plaintext:

        transposition_matrix[i][j] = char

        j += 1

        if j >= (len(transposition_matrix[0])):
            j = 0
            i += 1

    for j in range(len(transposition_matrix[0])):

        for i in range(transposition_key):

            plaintext += transposition_matrix[i][j]

    return plaintext

# Fungsi-fungsi affine cipher

def affineEncrypt(plaintext:str, m:int, b:int):

    plaintext_preprocessed = preprocess(plaintext)

    ciphertext = ""

    for char in plaintext_preprocessed:

        c = chr(((m * (ord(char) - ord("A")) + b) % 26) + ord("A"))
        ciphertext += c

    return ciphertext

def affineDecrypt(ciphertext:str, m:int, b:int):

    ciphertext_preprocessed = preprocess(ciphertext)

    plaintext = ""

    for char in ciphertext_preprocessed:

        p = chr(((pow(m, -1, 26) * (ord(char) - ord("A") - b)) % 26) + ord("A"))
        plaintext += p
    
    return plaintext

# Fungsi-fungsi autokey vigenere

def vigenereAutokeyEncrypt(plaintext:str, key:str):

    plaintext_preprocessed = preprocess(plaintext)
    key_preprocessed = preprocess(key)

    ciphertext = ""
    i = 0

    for char in plaintext_preprocessed:

        c = chr(((ord(char) + ord(key_preprocessed[i])) % 26) + ord("A"))

        ciphertext += c
        key_preprocessed += char

        i += 1

    return ciphertext

def vigenereAutokeyDecrypt(ciphertext:str, key:str):

    ciphertext_preprocessed = preprocess(ciphertext)
    key_preprocessed = preprocess(key)

    plaintext = ""
    i = 0

    for char in ciphertext_preprocessed:

        p = chr(((ord(char) - ord(key_preprocessed[i])) % 26) + ord("A"))

        plaintext += p
        key_preprocessed += p

        i += 1

    return plaintext