def split(word):
    return [char for char in word]

file1 = open('input.txt', 'r')
firststack = [0]

line = file1.readline()
wordlist = split(line)
for word in wordlist:  
    if word == '-':
        firststack[len(firststack)-1] -= 1
    elif word == '+':
        firststack[len(firststack)-1] += 1
    elif word == '>':
        tempval = firststack[0]
        del firststack[0]
        firststack.append(tempval)
    elif word == '<':
        tempval = firststack[len(firststack)-1]
        del firststack[len(firststack)-1]
        firststack.insert(0, tempval)
    elif word == '@':
        tempval = firststack[len(firststack)-1]
        firststack[len(firststack)-1] = firststack[len(firststack)-2]
        firststack[len(firststack)-2] = tempval
    elif word == '.':
        firststack.append(firststack[len(firststack)-1])

file1.close()

for char in firststack:
    print(chr(char), end="")


