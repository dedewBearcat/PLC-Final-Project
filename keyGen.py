import random

def keyGen(seeder):
    key = []
    random.seed(seedGen(seeder))
    translated = [] #record of all characters already assigned to an uncoded character
    for i in range(32,126): #32,126 is regular text characters in ASCII
        v = (i + random.randint(1,1000)) % 127 #%127 makes sure that the character is within the upper bound of text characters in ascii
        while v in translated or v < 32: #If v is already assigned to an uncoded character or if v is not within the bounds of regular text characters, it'll reroll the character
            v = (i + random.randint(1,1000)) % 127
        translated += [v]
        key.append([chr(i), chr(v)]) #appends to key the uncoded character and it's coded character subsequently
    return key

def seedGen(seeder):
    seed = 0
    for c in seeder: #unicodifies whatever string the seeder gave
        seed += ord(c) #seed becomes the sum of all unicode code
    return seed
