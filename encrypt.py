import keyGen
import datetime

def __encrypt(path, seeder = None):
    datetimer = str(datetime.datetime.now())
    codedmessage = ""
    if seeder is None: #if no seed is given, use the datetime to call keyGen
        key = keyGen.keyGen(datetimer)
    else: #else calls keyGen using the user given seeder
        key = keyGen.keyGen(seeder)
    file = open(path, "r")
    for line in file: #rewrites character by character from file to codedmessage string var
        uncodedmessage = line.strip()
        for char in uncodedmessage:
            for sub in key:
                if char == sub[0]:
                    codedmessage += sub[1]
        codedmessage += "\n"
    try: #writes codedmessage into the new text file
        filename = path.replace(".txt", "")
        with open(filename + "_coded.txt", "x") as output:
            output.write(datetimer)
            output.write("\n")
            output.write(codedmessage)
            result = f"Message has been successfully coded. Look for {filename}_coded.txt." #results to print
    except FileExistsError:
        result = f"File by {filename}_coded.txt already exists. Encoding process cancelled." #results to print
    print(result)
    return result
