#Johnny Catullo, SEC Internship, Set 2 Problem 12 Cyrptopals
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode,b64decode
from Set2Problem9 import Pad

appendedEncryption = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
key = None

def encryptionoracle(plaintext):
    global key
    #Randomize key
    if key is None:
        key = get_random_bytes(16)
    
    cipher = AES.new(key,AES.MODE_ECB)

    plaintext = Pad((plaintext + b64decode(appendedEncryption)),16)

    return cipher.encrypt(plaintext)

#Returns lenght of a block for the cipher used by the encryption oracle
def findBlockSize(encryptionOracle):
    text = b''

    ciphertext = encryptionoracle(text)
    initlen = len(ciphertext) #initial length
    newlength = initlen

    while newlength == initlen:
        text += b'A'
        ciphertext = encryptionoracle(text)
        newlength = len(ciphertext)

    
    return newlength - initlen

def confirmECB(encryptionOracle, blocksize):
    size = get_random_bytes(blocksize) * 2
    encryption = encryptionoracle(size)

    if encryption[0:blocksize] != encryption[blocksize:2*blocksize]:
        print("Not using ECB!")

#Find next byte of the message
def getNextByte(encryptionoracle, blocksize, knownbytes):
    size = bytes([0] * (blocksize - (len(knownbytes) % blocksize) - 1))
    d = {}

    for i in range(256):
        cipher = encryptionoracle(size + knownbytes + bytes([i]))
        d[cipher[0:len(size) + len(knownbytes) + 1]] = i

    cipher = encryptionoracle(size)
    u = cipher[0:len(size) + len(knownbytes) + 1]

    if u in d:
        return d[u]
    
    return None


if __name__ == '__main__':
    blocksize = findBlockSize(encryptionoracle)
    confirmECB(encryptionoracle,blocksize)
    cipher = b''
    while True:
        byt = getNextByte(encryptionoracle,blocksize,cipher)
        if byt is None:
            break
        cipher += bytes([byt])
    print(cipher)
    


