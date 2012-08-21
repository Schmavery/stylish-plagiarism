import string

thesaurusFile = open("thesaurus.txt")
thes2File = open("thesausus2.txt", "w+")

for line in thesaurusFile:
    #print line
    words = string.split(line)
    firstWord = words[0]
    if (len(firstWord) > 2):
        thes2File.write(line)

thes2File.close()
