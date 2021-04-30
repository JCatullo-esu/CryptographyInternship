#Johnny Catullo, SEC Internship, Set 2 Problem 11 Cyrptopals
from Crypto.Cipher import AES
from Crypto import Random
from Set2Problem9 import Pad
from Set2Problem10 import AESEncrypt, CBCEncrypt
from random import randint


def encryptionoracle(plaintext):
    #Generate random key using Crypto's Random library
    key = Random.new().read(AES.block_size)
    plaintextpadded = randomPad(plaintext)

    #50/50 chance to decide whether to encrypt the plaintext by CBC or EBC
    if randint(0,1) == 0:
        ECB = AESEncrypt(plaintextpadded,key)
        encryptionused = "ECB"
        return ECB,encryptionused
    else:
        #Generate random IV
        IV = Random.new().read(randint(5,10))

        CBC = CBCEncrypt(plaintextpadded,IV,key)
        encryptionused = "CBC"
        return CBC,encryptionused

#Padding before and after the plaintext randomly by 6-10 bytes
def randomPad(plaintext):
    return Random.new().read(randint(5,10)) + plaintext + Random.new().read(randint(5,10))

def detectEncryption(cipher):
    if cipher[16:32] == cipher[32:48]:
        return "ECB"
    else:
        return "CBC"

if __name__ == '__main__':
    plaintext = bytes([0]*64)

    encrypt = encryptionoracle(plaintext)
    print(encrypt)
    detectEncryption(encrypt)

