import numpy as np
import json
import sys

ogFile = sys.argv[1]
# ogFile = "data/cleanmyspace.txt"
randomDataset = sys.argv[2]
# randomDataset = "data/cleanRockYou.txt"
choicePercent = int(sys.argv[3])
# choicePercent = 0.1

print("Choice percent is " + str(choicePercent) + "%")
print(int(choicePercent))

with open(ogFile, encoding='latin1') as f:
    newP = f.readlines()
ogWords = np.array(newP)

print("Length of original words is: " + str(len(ogWords)))

with open(randomDataset, encoding='latin1') as f:
    newR = f.readlines()
randomWords = np.array(newR)

randomChoice = int(len(ogWords) * (choicePercent/100))


print("Number of words to add is: " + str(randomChoice))
if randomChoice < len(randomWords):
  AddingWords = np.random.choice(a=randomWords, size=randomChoice, replace=False)
  # print(AddingWords)

  for word in AddingWords:
      if word in ogWords:  # we have to get a new one
          alreadyInFlag = True
          
          while alreadyInFlag:
              print(str(word) + " Word already in ogWords")
              newRandom = np.random.choice(a=randomWords, size=1, replace=False)
              print(newRandom)
              if newRandom not in ogWords:
                  ogWords = np.append(ogWords, newRandom)
                  alreadyInFlag = False
      else:
          ogWords = np.append(ogWords, word)
else:
  print("Other file is too small for random choice, adding all non duplicates")
  main_list = list(set(randomWords) - set(ogWords))
  print("Adding " + str(len(main_list)))
  print(main_list)
  ogWords = np.append(ogWords, main_list)
  print(ogWords)



newFileName = "data/" + ogFile.split("/")[1].split(".txt")[0] + "Extended_" + str(choicePercent) + "_" + randomDataset.split("/")[1].split(".txt")[0] + ".txt"

print("New length of words is " + str(len(ogWords)))
finalWords = list(ogWords)
print("New filename is " + str(newFileName))
with open(newFileName, 'w', encoding='latin1') as f:
    # f.write(json.dumps(finalWords))
    f.writelines(finalWords)
    #for w in finalWords:
    #    f.write('%s\n' % w)
    #    f.write(str(finalWords))

print("Done")
