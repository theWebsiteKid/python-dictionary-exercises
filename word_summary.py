message = raw_input("What's happening?: ")
newDict = {}

word_list = message.split(" ")

for word in word_list:
    if word not in newDict:
        newDict[word] = 1
    else:
        newDict[word] += 1

print newDict
