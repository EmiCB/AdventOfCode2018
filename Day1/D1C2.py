input = open("D1C1InputTest.txt", "r")
frequencies = []
lastFreq = 0

for line in input:
    lastFreq += int(line)
    for x in frequencies:
        if(x == lastFreq):    # and (frequencies.index(x) != (len(frequencies)-1))
            print(lastFreq)
        else:
            frequencies.append(lastFreq)