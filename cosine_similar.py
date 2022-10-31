import math
from collections import Counter
import pandas as pd
import time

'''
This file is used to determine the cosine similarity of the two datasets together. The ogFiles is an array of files
and the sampleFile is the new file to be tested.
'''

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0) ** 2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0) ** 2 for k in terms))
    cosineSimilar = dotprod / (magA * magB)
    # print("Cosine similar:")
    # print(cosineSimilar)
    return cosineSimilar

def similarity_score(l1, l2):
    c1, c2 = Counter(l1), Counter(l2)
    return counter_cosine_similarity(c1, c2)

ogFiles = ["data/cleanrichelieutop20000.txt", "data/cleanmyspace.txt", "data/cleanRockYou.txt", "allSamples/richelieutop20000_50000_50mil.txt", "allSamples/cleanMySpaceBetter_50mil.txt"]
# sampleFile = sys.argv[2]
sampleFile = "allSamples/RockYouFinal_50000_50mil.txt"  # "allSamples/richelieutop20000_50000_50mil.txt"  # sys.argv[1]

totalText = ""

with open(sampleFile, 'r', encoding='latin1') as f:
    lines = f.readlines()
allWords = pd.DataFrame(lines)

print("Evaluating Sample file: " + str(sampleFile.split('/')[1].replace(".txt", "")))
totalText += "Evaluating Sample file: " + str(sampleFile.split('/')[1].replace(".txt", ""))


for otherFile in ogFiles:
    with open(otherFile, 'r', encoding='latin1') as f:
        lines = f.readlines()
    otherWords = pd.DataFrame(lines)
    similarScore = similarity_score(allWords[0], otherWords[0])
    print("File: " + str(otherFile.split('/')[1].replace(".txt", "")) + " has score of " + str(similarScore))
    totalText += "\nFile: " + str(otherFile.split('/')[1].replace(".txt", "")) + " has score of " + str(similarScore)


nowTime = time.strftime("%m_%d")
with open("passwordEvaluations/NewCosineSimilarity_" + sampleFile.split('/')[1].replace(".txt", "") + "_" + nowTime + ".txt", 'w+') as f:
    f.write(totalText)