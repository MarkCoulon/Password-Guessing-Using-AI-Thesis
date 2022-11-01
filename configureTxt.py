import sys
# filename = "data/myspace.txt"
# newfilename = "data/cleanmyspace.txt"
filename = sys.argv[1]
newfilename = sys.argv[2]

with open(filename, 'r', encoding='latin-1') as f:
    lines = f.readlines()

print("Length of file: " + str(len(lines)))
new_list = [x for x in lines if len(x) <= 10]

print("Length of file after removal: " + str(len(new_list)))
i = 0
for word in new_list:
    for letter in word:
        if ord(letter) > 128:
            print("error")
            print(str(i) + "/" + str(len(lines)))
            lines.remove(word)
            break
    i += 1

print("writing")
print("Length of file after removal2: " + str(len(new_list)))

with open(newfilename, 'w') as f:
    f.write(''.join(new_list))




print("done")
    
