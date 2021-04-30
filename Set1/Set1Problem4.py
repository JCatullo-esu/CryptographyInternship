#Johnny Catullo, SEC Internship, Set 1 Problem 4 Cyrptopals
from binascii import unhexlify
from Set1Problem3 import freqScore, SingleByteXOR



if '__main__' == __name__:

    #Stores potential plaintexts from bruteforcing
    potential_plaintext = []

    #Open and Read file
    with open('Problem4CipherText.txt','r') as file:

        for line in file.readlines():
            #Formats lines for unhexlify
            if line[-1] == '\n':
                line = line[:-1]
            unhexCipher = unhexlify(line)
  
            for key_val in range (256):
                plaintext = SingleByteXOR(unhexCipher,key_val)
                score = freqScore(plaintext)

                #Stores the message, frequency score and the key value
                data = {
                    'message': plaintext,
                    'score': score,
                    'key': key_val
                }

                potential_plaintext.append(data)

           #Store best score in array
            best_score = sorted(potential_plaintext, key=lambda x: x['score'], reverse=True)[0]
    
        for item in best_score:
            print("{}: {}".format(item.title(), best_score[item]))





        

        