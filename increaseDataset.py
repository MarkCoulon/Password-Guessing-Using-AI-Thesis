import numpy as np
import json

'''
this file is used to increase the dataset of a file based on a choicePercentage, e.g. 0.1 means 10%. The ogFile is the
original file and the randomDataset is the file that the new passwords will come from
'''

ogFile = "data/cleanmyspace.txt"
randomDataset = "data/cleanRockYou.txt"
choicePercent = 0.1

with open(ogFile, encoding='latin1') as f:
    newP = f.readlines()
ogWords = np.array(newP)

print("Length of original words is: " + str(len(ogWords)))

with open(randomDataset, encoding='latin1') as f:
    newR = f.readlines()
randomWords = np.array(newR)

randomChoice = int(len(ogWords) * choicePercent)
# randomChoice = 5

print(ogWords)
print("Number of words to add is: " + str(randomChoice))
AddingWords = np.random.choice(a=randomWords, size=randomChoice, replace=False)

print(AddingWords)

for word in AddingWords:
    if word in ogWords:  # we have to get a new one
        alreadyInFlag = True
        print(word)
        while alreadyInFlag:
            print("Word already in ogWords")
            newRandom = np.random.choice(a=randomWords, size=1, replace=False)
            print(newRandom)
            if newRandom not in ogWords:
                ogWords = np.append(ogWords, newRandom)
                alreadyInFlag = False
    else:
        ogWords = np.append(ogWords, word)

newFileName = ogFile.split("/")[1].split(".txt")[0] + "Extended.txt"

print("New length of words is " + str(len(ogWords)))
finalWords = list(ogWords)
with open(newFileName, 'w', encoding='latin1') as f:
    # f.write(json.dumps(finalWords))
    f.writelines(finalWords)
    #for w in finalWords:
    #    f.write('%s\n' % w)
    #    f.write(str(finalWords))

print("Done")