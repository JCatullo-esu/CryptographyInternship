#Johnny Catullo, SEC Internship, Set 1 Problem 3 Cyrptopals
from binascii import unhexlify


#Decode one byte at a time
ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

#Compares each byte to the score
def freqScore(input):
    #Use character freq to help find the most likely key from bruteforcing
    #From greatest to least frequent letters used in the alphabet
    #sc: https://en.wikipedia.org/wiki/Letter_frequency
    charfreq = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([charfreq.get(chr(byte),0) for byte in input.lower()])


#Single Byte XOR function, cant use bxor because it does not XOR byte by char
def SingleByteXOR(input,charval):
    output = b''

    for byte in input:
        output += bytes([byte ^ charval])
    return output

def SingleByteXORBruteForce(ciphertext):
    #Stores potential plaintexts from bruteforcing
    potential_plaintext = []

    #Bruteforces the unhexed byte string
    for key_val in range (256):
        plaintext = SingleByteXOR(ciphertext,key_val)
        score = freqScore(plaintext)

        #Stores the message, frequency score and the key value
        data = {
            'message': plaintext,
            'score': score,
            'key': key_val
        }

        potential_plaintext.append(data)
        
    #Determines out of the potential plaintext array if the plaintext has the highest score
    best_score = sorted(potential_plaintext, key=lambda c: c['score'],reverse=True)[0]

    for item in best_score:
        print("{}: {}".format(item.title(), best_score[item]))

    return best_score


if '__main__' == __name__:

    #Decode from Hex
    unhexCipher = unhexlify(ciphertext)

    SingleByteXORBruteForce(unhexCipher)
    
   

    
    
    