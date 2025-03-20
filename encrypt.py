import keyGen
import datetime

def __encrypt(filename, seeder = None):
    datetimer = str(datetime.datetime.now())
    file = open(filename, "r")
    codedmessage = ""
    if seeder is None:
        key = keyGen.keyGen(datetimer)
    else:
        key = keyGen.keyGen(seeder)
    for line in file:
        uncodedmessage = line.strip()
        for char in uncodedmessage:
            for sub in key:
                if char == sub[0]:
                    codedmessage += sub[1]
        codedmessage += "\n"
    try:
        filename = filename.replace(".txt", "")
        with open(filename + "_coded.txt", "x") as output:
            output.write(datetimer)
            output.write("\n")
            output.write(codedmessage)
            print(f"Message has been successfully coded. Look for {filename}_coded.txt.")
    except FileExistsError:
        print(f"File by {filename}_coded.txt already exists. Encoding process cancelled.")

__encrypt("testmessage1.txt", "Isnt this string")
