n = open("outputFile.txt","r")  # open file, read-only
s = open("outputSorted.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()
