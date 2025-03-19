import random

def keyGen(seeder):
    key = []
    random.seed(seedGen(seeder))
    translated = []
    for i in range(32,126):
        v = (i + random.randint(1,1000)) % 127
        while v in translated or v < 32:
            v = (i + random.randint(1,1000)) % 127
        translated += [v]
        key.append([chr(i), chr(v)])
    return key

def seedGen(seeder):
    seed = 0
    for c in seeder:
        seed += ord(c)
    return seed
