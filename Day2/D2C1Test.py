input = open("D2C1InputTest.txt", "r")
lineLetters = []
currentLine = ""
doubles = 0
triples = 0
checksum = 0
nxt = 1
isDoubleAvailable = True
isTrippleAvailable = True

for line in input:
    currentLine = str(line)

    for letter in currentLine:
        lineLetters.append(str(letter))

    for entry in lineLetters:
        if entry == "\n":
            lineLetters.remove(entry)
    lineLetters.sort()
    lineLetters.append(" ")

    isDoubleAvailable = True
    isTrippleAvailable = True
    print(lineLetters)

    for l in lineLetters:
        if l != " ":
            if isDoubleAvailable and l == lineLetters[lineLetters.index(l)+1] and l != lineLetters[lineLetters.index(l)+2]:
                    isDoubleAvailable = False
                    doubles += 1
            if isTrippleAvailable and l == lineLetters[lineLetters.index(l)+1] and l == lineLetters[lineLetters.index(l)+2]:
                    isTrippleAvailable = False
                    triples += 1

    lineLetters.clear()
    
checksum = doubles * triples
print("Doubles: " + str(doubles))
print("Triples: " + str(triples))
print("Checksum: " + str(checksum))