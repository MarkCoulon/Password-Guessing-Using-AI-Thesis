import numpy as np
from collections import Counter
import time
import sys

ogFiles = ["data/cleanrichelieutop20000.txt", "data/cleanmyspace.txt", "data/cleanRockYou.txt"] # , "data/cleanrichelieutop20000Extended_30_cleanmyspace.txt"
# sampleFile = sys.argv[2]
sampleFile = "allSamples/Richelieu_50000_25mil.txt"  # sys.argv[1]

# loop through all the data files,
# find all the intersecting ones for each datafile with the sample file
totalText = ""
print("Sample file: " + str(sampleFile.split('/')[1].replace(".txt", "")))
totalText += "Sample file: " + str(sampleFile.split('/')[1].replace(".txt", ""))
with open(sampleFile, encoding='latin1') as f:
    newP = f.readlines()
nnewP = np.array(newP)

print("length of samples: " + str(len(nnewP)))
totalText += "\nlength of samples: " + str(len(nnewP))
# remove duplicates, does not seem to affect % of passwords found with all passwords
uniqueNnewP = len(np.unique(nnewP))
print("length of unique samples: " + str(uniqueNnewP))
totalText += "\nlength of unique samples: " + str(uniqueNnewP)

# finding duplicates
duplicates = len([item for item, count in Counter(nnewP).items() if count > 1])
print("number of duplicates: " + str(duplicates) + "/" + str(len(nnewP)))
totalText += "\nnumber of duplicates: " + str(duplicates) + "/" + str(len(nnewP))
print("number of duplicates percentage: " + str((duplicates / len(nnewP)) * 100) + " % are duplicates")
totalText += "\nnumber of duplicates percentage: " + str((duplicates / len(nnewP)) * 100) + " % are duplicates"

totalText += "\n\_________Description_________\n"
print("_________Description_________")
print("First number is the number of similar passwords out of the other dataset")
totalText += "\n" + "First number is the number of similar passwords out of the other dataset"
print("And this is the number of similar passwords out of it's own dataset")
totalText += "\n" + "And this is the number of similar passwords out of it's own dataset"

print("_________Start_________")
totalText += "\n_________Start_________\n"
for ogFile in ogFiles:
    totalText += "\nData File: " + str(ogFile)
    print("Data File: " + str(ogFile))
    with open(ogFile, encoding='latin1') as f:
        allP = f.readlines()
    # convert to numpy
    nallP = np.array(allP)

    print("length of all passwords: " + str(len(nallP)))
    totalText += "\nlength of all passwords: " + str(len(nallP))

    # using numpy to find intersects
    intersect = np.intersect1d(nallP, nnewP)  # uniqueNnewP
    passwordIndex = len(intersect)

    print(str(passwordIndex) + " passwords that are the same out of " + str(len(nallP)))
    totalText += "\n" + str(passwordIndex) + " passwords that are the same out of " + str(len(nallP))

    print(str(passwordIndex) + " sample passwords that are the same out of " + str(nnewP))
    totalText += "\n" + str(passwordIndex) + " sample passwords that are the same out of " + str(nnewP)

    print(str((passwordIndex / len(allP)) * 100) + " % of password with index / all passwords in dataset")
    totalText += "\n" + str((passwordIndex / len(allP)) * 100) + " % of password with index / all passwords in dataset"

    print(str((passwordIndex / len(nnewP)) * 100) + " % of password with index / unique sample passwords")
    totalText += "\n" + str((passwordIndex / len(nnewP)) * 100) + " % of password with index / unique sample passwords"

    totalText += "\n______________\n"

nowTime = time.strftime("%m_%d")
with open("passwordEvaluations/FinalPasswordEval_" + sampleFile.split('/')[1].replace(".txt",
                                                                                      "") + "_" + nowTime + ".txt",
          'w+') as f:
    f.write(totalText)