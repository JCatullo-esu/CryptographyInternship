#Johnny Catullo, SEC Internship, Set 1 Problem 5 Cyrptopals
from binascii import hexlify,unhexlify

#The plaintext that is given
plaintext = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b'ICE'

#The results when the cipher is completed sucessfully
expectCipher = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

#The repeating XOR function
def RepeatingXOR(ptext, key):
    #Intilization

    i = 0
    ciphertext = b''

    #For every byte in the plaintext, the key iterates through itself so each byte of the key XOR's the byte of the plaintext
    for byte in ptext:
        ciphertext += bytes([byte ^ key[i]])

        i = i + 1 if (i < len(key) - 1) else 0
    
    return ciphertext



#Check to see if the result matches the given ciphertext
def CipherCheck(cipher):
    if (cipher == expectCipher):
        print(b'Plaintext after conversion: ' + cipher)
        print("Ciphertext and expected ciphertext match, sucess!")
    else:
        print("Error: Ciphertext does not match the expected ciphertext")
        print(cipher)
        
        
if '__main__' == __name__:

    ciphertext = RepeatingXOR(plaintext,key)
   
    hextext = hexlify(ciphertext)


    print(b'Expected ciphertext: ' + expectCipher)


    CipherCheck(hextext)


    
 
