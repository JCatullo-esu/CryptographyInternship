#Johnny Catullo, SEC Internship, Set 2 Problem 9 Cyrptopals

def Pad(plaintext,size):

    #If the plaintext is equal to the pad size, return message
    if (len(plaintext) == size):
        return plaintext

    #Compute how much padding is needed 
    blocksize = size - len(plaintext)

    #Find the remainder and add bytes to the original message
    padding = blocksize % size
    return plaintext + bytes([padding]*padding)

if '__main__' == __name__:
   message = b'YELLOW SUBMARINE'

   print(Pad(message,20))
    
