from zxcvbn import zxcvbn
import numpy as np
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import sys

'''
https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
'''

'''
For a file of 9,886,636 takes about 1 hour and 11 minutes to run
all samples should be around 10 million, so should take the same time
all samples are now around 50 mil, so it will take 5 times longer fml
'''

filename = "allSamples/cleanMySpaceBetter_50mil.txt"
newFileName = "strengthScores/" + filename.split("/")[1].split('.txt')[0] + "Score.txt"
pltFileName = "distributions/" + filename.split("/")[1].split('.txt')[0] + "Dist.png"

print("Getting rid of blank lines")
with open(filename, 'r', encoding='latin1') as f:
    lines = f.readlines()

print("writing")
with open(filename, 'w', encoding='latin1') as f:
    for line in lines:
        if not line.isspace():
            f.write(line)
print("done")

with open(filename, 'r', encoding='latin1') as f:
    lines = f.readlines()

print("convert to numpy")
nArray = np.array(lines)
print("remove newlines")
remArray = np.char.strip(nArray, '\n')

scores = {}
allScores = 0
count = 0
scores['0'] = 0
scores['1'] = 0
scores['2'] = 0
scores['3'] = 0
scores['4'] = 0

print("Finding scores")
for elem in tqdm(remArray):
    all = zxcvbn(str(elem))
    scores[str(all['score'])] += 1
    allScores += all['score']
    count += 1

print("finding mean")
mean = allScores / count
print(mean)

with open(newFileName, 'w', encoding='latin1') as f:
    f.write("Mean is: " + str(mean) + "\n")
    f.write(json.dumps(scores))

print("Done calculation, doing histogram now")


with open(newFileName, 'r', encoding='latin1') as f:
    lines = f.readlines()

mean = lines[0]
passwords = json.loads(lines[1])


passwordValues = list(passwords.values())
zeroScore = passwords['0']
oneScore = passwords['1']
twoScore = passwords['2']
threeScore = passwords['3']
fourScore = passwords['4']
totalScores = zeroScore + oneScore + twoScore + threeScore + fourScore
countScores = [zeroScore, oneScore, twoScore, threeScore, fourScore]
print("making histogram")

fig, ax = plt.subplots(figsize=(8,8))
bars = ax.bar([0, 1, 2, 3, 4], countScores)
plt.title(filename.split("/")[1].split(".txt")[0])
plt.xlabel("Scores")
plt.ylabel("Count")
barYCenter = ax.get_yticks()[1] * 0.25
i = 0
for bar in bars:
    width = bar.get_width()
    height = bar.get_height()
    x, y = bar.get_xy()
    plt.text(x+width/2, barYCenter,
             str(countScores[i]) + " (" + str(round(countScores[i] / totalScores * 100, 2)) + "%)",
             rotation_mode='anchor', rotation=90)
    i += 1


plt.savefig(pltFileName)
plt.show()
