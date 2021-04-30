#Johnny Catullo, SEC Internship, Set 1 Problem 6 Cyrptopals
import sys
from functools import reduce
from base64 import b64decode
from binascii import hexlify,unhexlify
from itertools import combinations
from Set1Problem2 import bxor
from Set1Problem5 import RepeatingXOR
from Set1Problem3 import SingleByteXORBruteForce,freqScore


#Counts the byte difference between two strings
def HammingDistance(String1,String2):
    return(sum(bin(byte).count('1') for byte in bxor(String1,String2)))


def repeatingKeyXor(cipher):
    normalDist = {}

    #Keysize guess length between 2 ~ 40
    for keysize in range (2,40):

        #Take 4 KEYSIZE blocks instead of 2 and average the distances.
        blocks = [cipher[i:i + keysize] for i in range (0, len(cipher), keysize)][:4]

        #Sum hamming distance
        distance = 0
        pairs = combinations(blocks, 2)
        for (x,y) in pairs:
            distance += HammingDistance(x,y)

        #Getting average distance
        distance /= 6

        #Normalize avg distance by dividing by keysize
        normalDistance = distance / keysize

        #Store norm distance
        normalDist[keysize] = normalDistance

    
    possibleKeys = sorted(normalDist,key = normalDist.get)[:3]
    possiblePlaintexts = []

    #Find the top 3 most likely keys
    for i in possibleKeys:
        #Set up for bytes
        key = b''

        for j in range(i):
            block = b''

            #Transpose blocks
            for k in range (j, len(cipher), i):
                block += bytes([cipher[k]])

            #Solve the block with single byte XOR
            key += bytes([SingleByteXORBruteForce(block)['key']])

        #Store potneital plaintexts
        possiblePlaintexts.append((RepeatingXOR(cipher,key), key))

    #Return the plaintext with the max english score
    return max(possiblePlaintexts, key=lambda k: freqScore(k[0]))

if '__main__' == __name__:

    #Decode the file from base64 
    with open ("Problem6CipherText.txt") as inputfile:
        data = b64decode(inputfile.read())

    result = repeatingKeyXor(data)


    print("Key =", result[1].decode())
    print("==========================")
    print(result[0].decode().rstrip())
   
    
    
    
    