#Johnny Catullo, SEC Internship, Set 1 Problem 8 Cyrptopals
from Crypto.Cipher import AES
from base64 import b64decode
from binascii import hexlify,unhexlify


#Gets chunks of x sized blocks
def chunks(ciphertext,x):
    return [ciphertext[i:i+x] for i in range (0,len(ciphertext),x)]

#Detects the repeating blocks
def ECBRepeating(f):
    BlockSize = 16

    with open (str(f),'rb') as file:
        
        for line in file.readlines():
            ciphertext = line.strip()
           
            #Group and count repeating chunks
            for i, line in enumerate(ciphertext):
            
                chunk = chunks(ciphertext,BlockSize)

                uniquechunks = set(chunk) 

                dupes = len(chunk) - len(uniquechunks)

    
                if dupes > 0:
                    ECB_line = (i,chunk)
                    
                    print(f'The ECB encrypted line is line no.  {(i)}:\n\n{chunk}')
                    return (i,chunks)
                
    
        file.close()
 



if '__main__' == __name__:

    ECBRepeating('Problem8CipherText.txt')

   