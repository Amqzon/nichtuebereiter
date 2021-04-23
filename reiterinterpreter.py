import random

überreiter = {
    "zeigan":print,
    "zufall":random.randint,
    "mathe":eval,
    "schreibe":eval,
    "liste":eval
    }

filename = "ueber.reiter"

with open(filename) as f:
    content = f.readlines()

for line in content:
    
    x = line.split("_")
    
    if line.startswith("premiumzeigan"):
        x2 = line.split(";")
        varinput = x2[1].split("{")
        eingabe = ""
        for i in varinput[1]:
            if i == "}":
                break
            else:
                eingabe = eingabe + i
        if x2[0].endswith("zufall"):
            zufallinput = eingabe.split(",")
            zffer = (varinput[0] + str(random.randint(int(zufallinput[0]),int(zufallinput[1]))))
            print(zffer)

        if x2[0].endswith("mathe"):
            print(varinput[0] + str(eval(eingabe)))
            
    
    if line.startswith("zeigan"):
        überreiter[x[0]](x[1])

    if line.startswith("zufall"):
        x2 = x[1].split(",")
        print(überreiter[x[0]](int(x2[0]),int(x2[1])))
    
    if line.startswith("mathe"):
        ergebnis = überreiter[x[0]]("print(" + x[1]+ ")")
    
    if line.startswith("schreibe"):
        speicherarg = x[1].split(";")
        f = open(speicherarg[0],speicherarg[1])
        f.write(speicherarg[2])
        f.close()
    if line.startswith("liste"):
        trennung = x[1]
        reiterliste = überreiter[x[0]]