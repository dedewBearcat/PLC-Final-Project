import random

def keyGen(seed):
    key = {}
    random.seed(seed)
    for i in range(32,126):
        v = (i + random.randint(1,1000)) % 127
        while v in key.values() or v < 32:
            v = (i + random.randint(1,1000)) % 127
        key[chr(i)] = chr(v)
    reversedKey = {v:k for k,v in key.items()}
    key = {v:k for k,v in reversedKey.items()}
    return key

def seedGen(choice, seeder):
    seed = 0
    match choice:
        case 1:
            for c in seeder:
                seed += ord(c)
    return keyGen(seed)
