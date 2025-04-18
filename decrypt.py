import keyGen

def __decrypt(path, seeder = None):
    file = open(path, "r")
    uncodedmessage = ""
    if seeder is None:
        seeder = file.readline()
        seeder = seeder.strip()
    else:
        file.readline()
    key = keyGen.keyGen(seeder)
    for line in file:
        codedmessage = line.strip()
        for char in codedmessage:
            for sub in key:
                if char == sub[1]:
                    uncodedmessage += sub[0]
        uncodedmessage += "\n"
    try:
        newfilename = path.replace(".txt", "")
        with open(newfilename + "_decoded.txt", "x") as output:
            output.write(uncodedmessage)
            result = f"Message has been successfully decoded. Look for {newfilename}_decoded.txt."
    except FileExistsError:
        result = f"File by {newfilename}_decoded.txt already exists. Decoding process cancelled."
    print(result)
    return result
