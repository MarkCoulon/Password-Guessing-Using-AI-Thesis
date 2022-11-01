import pandas as pd
import numpy as np

def strip_ascii(text):
    return "".join(char for char in text if char.isascii())  # ord(char) < 127) #  or char in "\n"

# filename = "data/cleanRockYou.txt"
filename = "11_4_samples_large.txt"


with open(filename) as f: # , encoding='latin1'
    lines = f.readlines()

print("read the lines with length " + str(len(lines)))

# using pandas
df = pd.Series(lines, name="values")

newDF = df.to_frame()

newDF['values'] = newDF.apply(lambda row: strip_ascii(row['values']), axis = 1)

print(newDF)

npArray = newDF.to_numpy()
print("numpy")
print(npArray)

content = str(npArray)
print("Content")
print(content)

with open("11_4_samples_done.txt", 'w') as f:
    f.writelines(content)

