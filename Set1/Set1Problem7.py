#Johnny Catullo, SEC Internship, Set 1 Problem 7 Cyrptopal
#This code will be using the AES library for convience 
#https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from Crypto.Cipher import AES
from base64 import b64decode

key = b'YELLOW SUBMARINE'

def AESdecryption(ciphertext):

    plaintext = ""

    #Using ECB
    cipher = AES.new(key,AES.MODE_ECB)
    plaintext_bytes = cipher.decrypt(ciphertext)
    plaintext = plaintext_bytes.decode()

    return plaintext
  


if '__main__' == __name__:

    #Open the file in binary
    with open ("Problem7CipherText.txt",'rb') as file:
    
        ciphertext = b64decode(file.read()).rstrip()
        print(AESdecryption(ciphertext))
        file.close()


