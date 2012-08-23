import string, random

def TestSyn(syn, end):
    ## return basic ending, end minus 'e' and syn with double last letter
    synList = [syn+end, syn+syn[-1:]+end]
    if (syn[-1] == 'e'):
        synList.append(syn[:-1]+end)

    return synList

def ReplaceAll(text, thes):
    finalList = []
    sampleList = string.split(text)
    for word in sampleList:
        if (word in thes):
            finalList.append(thes[word][random.randint(0,len(thes[word]) - 1)])
        else:
            finalList.append(word)
    finalText = string.join(finalList, " ")
    return finalText


thesFile = open("thesaurus2.txt")
wordListFile = open("missingword.txt")
wordFile = open("missingword.txt")
newFile = open("extra_thesaurus_words.txt", "w+")

ends = ["ly", "able", "er", "ed", "ing", "age", "y", "or", "er", "ant", "ist", "ness", "dom", "ence", "ance", "est"]

##Load thesaurus into dictionary with synonyms as tuples##
thes = {}
newthes = {}
    
for line in thesFile:
    #print line
    words = string.split(line)
    tempSynonyms = []
    firstWord = words[0] 
    for word in words:
        if (not word == firstWord):
            tempSynonyms.append(word)
    tempSynonyms = tuple(tempSynonyms)
    thes[firstWord] = tempSynonyms

##Load wordlist into list##
wordList = []
for line in wordListFile:
    #print line[:-1]
    wordList.append(line[:-1])

currLetter = ""
currCount = 0
totalWords = 0
for line in wordFile:
    if (not currLetter == line[0]):
        print currLetter + str(currCount)
        totalWords += currCount
        currCount = 0
        currLetter = line[0]
        
    line = line[:-1]
    #print line
    tempSyns = []
    for end in ends:        
        if (len(line) >= len(end) + 3 and tempSyns == []):
            if (line[-(len(end)):] == end):
                #print "matches ending"
                tempWord = line[:-(len(end))]
                
                if (tempWord in wordList and tempWord in thes):
                    #print "- basic match"
                    #tempSyns = []
                    for syn in thes[tempWord]:
                        for testSyn in TestSyn(syn, end):
                            if (testSyn in wordList):
                                #print "-- new syn: " + testSyn
                                tempSyns.append(testSyn)
                                break
                
                elif (tempWord + "e" in wordList and tempWord + "e" in thes):
                    #print "- e match"
                    tempWord += "e"
                    #tempSyns = []
                    for syn in thes[tempWord]:
                        for testSyn in TestSyn(syn, end):
                            if (testSyn in wordList):
                                #print "-- new syn: " + testSyn
                                tempSyns.append(testSyn)
                                break
                    
                elif (tempWord[-1] ==tempWord[-2] and tempWord[:-1] in wordList and tempWord[:-1] in thes):
                    #print "- double match"
                    tempWord = tempWord[:-1]
                    #tempSyns = []
                    for syn in thes[tempWord]:
                        for testSyn in TestSyn(syn, end):
                            if (testSyn in wordList):
                                #print "-- new syn: " + testSyn
                                tempSyns.append(testSyn)
                                break         
    if (not tempSyns == []):
        currCount += 1
        newthes[tempWord] = tuple(tempSyns)
        newFile.write(line.ljust(19," ") + string.join(tempSyns, " ") + "\n")
        tempSyns = []


running = True
mode = 0

newFile.close()

print "Total count: " + str(totalWords) + "\n"

while running:
    txtout = ""
    if (mode == 0):
        txtin = raw_input("Test a word: ")
        if (txtin == 1):
            mode = 1
        elif (txtin == 0):
            mode = 0
        elif (txtin == 'q'):
            running = False
            txtout = "Thank you for using the plagiariser"
        else:
            txtout = thes[txtin]
    elif (mode == 1):
        txtin = raw_input("Convert some text:\n")
        if (txtin == 1):
            mode = 1
        elif (txtin == 0):
            mode = 0
        elif (txtin == 'q'):
            running = False
            txtout = "Thank you for using the plagiariser"
        else:
            txtout = ReplaceAll[txtin]
    else:
        running = False
        txtout = "Thank you for using the plagiariser"
    print txtout
    
    
    
