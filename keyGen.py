import random

def keyGen(seed):
    key = {}
    random.seed(seed)
    for i in range(32,126):
        v = (i + random.randint(1,1000)) % 126
        while i in key or v < 32:
            v += 1
        key[chr(i)] = chr(v)
    return key

def seedGen(choice, seeder):
    seed = 0
    match choice:
        case 1:
            for c in seeder:
                seed += ord(c)
    return keyGen(seed)

#print(seedGen(1, "this is the seed"))
#print(seedGen(1, "this is the seed"))
#print(seedGen(1, "this is the seed"))