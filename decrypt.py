import keyGen

def decrypt(filename):
    file = open(filename, "r")
    uncodedmessage = ""
    seeder = file.readline()
    seeder = seeder.strip()
    key = keyGen.seedGen(1, seeder)
    print(key)
    reversedKey = {v:k for k,v in key.items()}
    dereversedKey = {v:k for k,v in reversedKey.items()}
    print(reversedKey) #Why does reversing the dictionary make a few things wrong the first time, but not the second time
    print(dereversedKey)
    for line in file:
        codedmessage = line.strip()
        for char in codedmessage:
            uncodedmessage += reversedKey[char]
        uncodedmessage += "\n"
    try:
        newfilename = filename.replace(".txt", "")
        with open(newfilename + "_decoded.txt", "x") as output:
            output.write(uncodedmessage)
            print(f"Message has been successfully decoded. Look for {newfilename}_decoded.txt.")
    except FileExistsError:
        print(f"File by {newfilename}_decoded.txt already exists. Decoding process cancelled.")
decrypt("testmessage1_coded.txt")
