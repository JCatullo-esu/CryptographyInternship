#Johnny Catullo, SEC Internship, Set 1 Problem 2 CryptoPals
from binascii import unhexlify,hexlify

plaintext = '1c0111001f010100061a024b53535009181c'

XORbytes = '686974207468652062756c6c277320657965'

expected = '746865206b696420646f6e277420706c6179'

#XORing bytes using byte arrays
def bxor(b1, b2):
     return bytes([ x^y for (x,y) in zip(b1, b2)])

if '__main__' == __name__:
    
    #Converts the byte string from hex
    unhexPlain = unhexlify(plaintext)
    unhexXOR = unhexlify(XORbytes)
    unhexExp = unhexlify(expected)

    #XOR the decoded plaintext and XOR byte string
    result = bxor(unhexPlain,unhexXOR)
    
    print("Expected: ")
    print(unhexExp)
    
    print("\n" + "Result: ")
    print(result)
    print("\n")
      
    #Check to see if they match
    if (result == unhexExp):
        print("Both of the cyphertexts match, success.")
    else:
        print("Error: Cyphertexts do not match")