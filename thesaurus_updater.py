import string

thesaurusFile = open("thesaurus.txt")
wordsFile = open("wordlist.txt")
missingFile = open("missingword.txt", "w+")

thes = {}

biggestWordSize = 0
for line in thesaurusFile:
    #print line
    words = string.split(line)
    tempSynonyms = []
    firstWord = words[0]
    if (len(firstWord) > biggestWordSize):
        biggestWordSize = len(firstWord)
    for word in words:
        if (not word == firstWord):
            tempSynonyms.append(word)
    tempSynonyms = tuple(tempSynonyms)
    thes[firstWord] = tempSynonyms

print "Biggest Thesaurus word: " + str(biggestWordSize)

currLetter = '0'
count = 0
biggestWordSize = 0
for line in wordsFile:
    if (len(line) > 4 and not line[0].isupper() and not line in thes and len(line) <= 14):
        if (not line[0] == currLetter):
            currLetter = line[0]
            print currLetter
        count += 1
        missingFile.write(line)
        if (len(line) > biggestWordSize):
            biggestWordSize = len(line)
print "total words: " + str(count)
print "Biggest Wordlist word: " + str(biggestWordSize)
missingFile.close
