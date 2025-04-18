import keyGen

def __decrypt(path, seeder = None):
    file = open(path, "r")
    uncodedmessage = ""
    if seeder is None: #if no seed is given, use the datetime which is always on the first line
        seeder = file.readline()
        seeder = seeder.strip()
    else: #since datetime is always on the first line, this gets rid of the first line so it doesn't go throught he decoding process
        file.readline()
    key = keyGen.keyGen(seeder) #calls on keyGen using the given seed or using the datetime
    for line in file: #rewrites character by character from file to codedmessage string var
        codedmessage = line.strip()
        for char in codedmessage:
            for sub in key:
                if char == sub[1]:
                    uncodedmessage += sub[0]
        uncodedmessage += "\n"
    try:#writes decodedmessage into the new text file
        newfilename = path.replace(".txt", "")
        with open(newfilename + "_decoded.txt", "x") as output:
            output.write(uncodedmessage)
            result = f"Message has been successfully decoded. Look for {newfilename}_decoded.txt." #results to print
    except FileExistsError:
        result = f"File by {newfilename}_decoded.txt already exists. Decoding process cancelled." #results to print
    print(result)
    return result
