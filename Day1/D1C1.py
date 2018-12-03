input = open("D1C1Input.txt", "r")
total = 0

for line in input:
    total += int(line)

print(total)