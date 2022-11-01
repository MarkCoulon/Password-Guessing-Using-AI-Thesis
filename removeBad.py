import pandas as pd
import sys

# filename = "data/myspace.txt"
# newFileName = "data/myspace.txt"  
# blankfilename = "data/myspace.txt"
filename = sys.argv[1]
newFileName = filename
blankfilename = filename

with open(filename, encoding='latin1') as f:
    lines = f.readlines()

i = 0
print("read the lines with length " + str(len(lines)))

for word in lines:
    if (i % 100000 == 0):
      print(str((i/len(lines)) * 100) + " %")
    # print(str(i) + "/" + str(len(lines)))
    for letter in word:
        # print(letter)
        if ord(letter) >= 128:
            #print("error with word " + str(word))
            #print(str(i) + "/" + str(len(lines)))
            lines.remove(word)
            break

    i += 1

print("writing")
with open(newFileName, 'w') as f: # "data/cleanRockYou.txt"
    f.write(''.join(lines))

print("removing blanks")
with open(blankfilename, 'r', encoding='latin1') as f:
    lines = f.readlines()

print("writing")
with open(blankfilename, 'w', encoding='latin1') as f:
    for line in lines:
        if not line.isspace():
            f.write(line)

print("done")
