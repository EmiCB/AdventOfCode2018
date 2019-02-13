input = open("D2C1Input.txt", "r")
lines = []
lineLetters = []
currentLine = ""
nextLine = ""
wrongCount = 0

correctID1 = ""
correctID2 = ""

# array of lines
for line in input:
    lines.append(str(line))

for l in lines:
    currentLine = l

    x = lines.index(l)
    if lines[x+1] != "":
        nextLine = lines[x+1]

        currentLine.replace("/n", " ")
        nextLine.replace("/n", " ")

        print(len(currentLine))
        print(len(nextLine))
        
        for n in range(0, len(currentLine)):
            if currentLine[n] != nextLine[n]:
                wrongCount += 1
        
        if wrongCount == 1:
            currentLine = correctID1
            nextLine = correctID2

    else:
        print("CorrectID1: " + correctID1)
        print("CorrectID2: " + correctID2)

    