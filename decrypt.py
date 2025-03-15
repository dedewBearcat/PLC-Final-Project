import keyGen

def decrypt(filename):
    file = open(filename, "r")
    uncodedmessage = ""
    seeder = file.readline()
    key = keyGen.seedGen(1, seeder)
    #todo implement key reversal
    for line in file:
        codedmessage = line.strip()
        for char in codedmessage:
            uncodedmessage += key[char]
        uncodedmessage += "\n"
    try: 
        with open(filename + "_coded.txt", "x") as output:
            output.write(codedmessage)
            print(f"Message has been successfully decoded. Look for {filename}_decoded.txt.")
    except FileExistsError:
        print(f"File by {filename}_decoded.txt already exists. Decoding process cancelled.")
 #implement filename .txt removal
decrypt("testmessage1.txt_coded.txt")