#Johnny Catullo SEC Internship, Set 2 Problem 10
from Crypto.Cipher import AES
from base64 import b64decode
from Set2Problem9 import Pad

key = b'YELLOW SUBMARINE'
IV = b'\x00' * AES.block_size #IV as long as the blocks it XORs against


def AESdecryption(ciphertext,key):

    plaintext = b''

    #Using ECB
    cipher = AES.new(key,AES.MODE_ECB)
    decryptcipher = cipher.decrypt(ciphertext)

    return unpad(decryptcipher)

#Used in Set1Problem2
def bxor(b1, b2):
     return bytes([ x^y for (x,y) in zip(b1, b2)])


#Will include AES and CBC Encryption for use of later Cyrptopals Problems
def AESEncrypt(plaintext,key):
    cipher = AES.new(key,AES.MODE_ECB)

    #Return the ciphered AES text with additional padding
    return cipher.encrypt(Pad(plaintext,AES.block_size))

def CBCEncrypt(plaintext,iv,key):
    ciphertext = b''
    vector = iv #Vector changes every block

    #Go about CBC block by block
    for i in range (0, len(plaintext), AES.block_size):

        #Pad the block before encrypting
        ptextblock = Pad(plaintext[i: i + AES.block_size], AES.block_size)

        #CBC Encryption
        blockcipher = bxor(ptextblock, vector)
        encryptedblock = AESEncrypt(blockcipher,key)
        ciphertext += encryptedblock
        vector = encryptedblock
    
    return ciphertext

#Check to see if the cipher is padded
def isPadded(cipher):
    padding = cipher[-cipher[-1]:]

    return all(padding[b] == len(padding) for b in range (0, len(padding)))

def unpad(cipher):
    if (len(cipher) == 0):
        return cipher

    if not isPadded(cipher):
        return cipher
    #Measure how much padding is in the string, and return the string minus the padding
    padding_len = cipher[len(cipher) - 1]
    return cipher[:-padding_len]


def CBCDecrypt(ciphertext,iv,key):
    plaintext = b''
    vector = iv

    for i in range (0, len(ciphertext),AES.block_size):
        ctextblock = ciphertext[i: i + AES.block_size] #Current text block
        decryptedblock = AESdecryption(ctextblock,key)
        plaintext += bxor(vector,decryptedblock)
        vector = ctextblock
    
    if unpad:
        return unpad(plaintext)
    else:
        return plaintext


if '__main__' == __name__:

    with open("Problem10Ciphertext.txt") as file:
        data = b64decode(file.read())

    print(CBCDecrypt(data,IV,key).decode().rstrip())



