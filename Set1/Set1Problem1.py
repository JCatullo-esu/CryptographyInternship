#Johnny Catullo, SEC Internship, Set 1 Problem 1 CryptoPals
import base64,binascii

#Given plaintext
plaintext = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

#Given ciphertext to check if conversion to b64 works
cyphertext = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

#Converts a hexidecimal bytes to a base 64 using libs
def hexToBase(hexString):
    decodedString = binascii.unhexlify(hexString)
    return base64.b64encode(decodedString).decode('ascii')

#Check to see if our ciphertexts matches the expected ciphertext
if '__main__' == __name__:
    print("The expected ciphertext: " + cyphertext + "\n")

    b64String = hexToBase(plaintext)

    print("The plaintext after conversion: " + b64String + "\n")

    #Check to see if they match
    if (b64String == cyphertext):
        print("Both of the cyphertexts match, success.")
    else:
        print("Error: Cyphertexts do not match")