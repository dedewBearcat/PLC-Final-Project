import keyGen
import datetime

def __encrypt(path, seeder = None):
    datetimer = str(datetime.datetime.now())
    codedmessage = ""
    if seeder is None:
        key = keyGen.keyGen(datetimer)
    else:
        key = keyGen.keyGen(seeder)
    file = open(path, "r")
    for line in file:
        uncodedmessage = line.strip()
        for char in uncodedmessage:
            for sub in key:
                if char == sub[0]:
                    codedmessage += sub[1]
        codedmessage += "\n"
    try:
        filename = path.replace(".txt", "")
        with open(filename + "_coded.txt", "x") as output:
            output.write(datetimer)
            output.write("\n")
            output.write(codedmessage)
            result = f"Message has been successfully coded. Look for {filename}_coded.txt."
    except FileExistsError:
        result = f"File by {filename}_coded.txt already exists. Encoding process cancelled."
    print(result)
    return result
