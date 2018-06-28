message = raw_input("What's happening?: ")
newDict = {}

for letter in message:
    if letter not in newDict:
        newDict[letter] = 1
    else:
        newDict[letter] += 1

print newDict
