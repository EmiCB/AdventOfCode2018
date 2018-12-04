input = open("D1C1Input.txt", "r")
frequencies = []
lastFreq = 0
stop = False

while stop == False:
    for line in input:
        lastFreq += int(line)
        if lastFreq in frequencies:
            print(lastFreq)
            stop = True
            break
        else:
            frequencies.append(lastFreq)
    input.seek(0)
    if(stop):
        break