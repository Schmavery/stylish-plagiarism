import cgi, webapp2, string, random

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <h1>The Stylish Plagiarizer</h1>
              <form action="/results" method="post">
                <div><input name="textbox" ></div>
                <div><input type="submit" value="Calculate"></div>
              </form>
            </body>
          </html>""")

class Compute(webapp2.RequestHandler):
    def post(self):
        
        thesFile = open("thesaurus.txt")

        sampleText = "Hunter fared poorly at the box office at the time of its release, making only $8.6 million in the United States."

        ##Load thesaurus into dictionary with synonyms as tuples##

        thes = {}
            
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


        ##Create and display altered text##
        running = True
        while running:

            sampleText = self.request.get('textbox')

            if (sampleText == 'q'):
                self.response.out.write("Thank you for using the Plagiariser.")
                running = False;
            else:
                finalList = []
                sampleList = string.split(sampleText)
                for word in sampleList:
                    if (word in thes):
                        finalList.append(thes[word][random.randint(0,len(thes[word]) - 1)])
                    else:
                        finalList.append(word)
                finalText = string.join(finalList, " ")
                
                self.response.out.write("\n\nPlagiarised:")
                self.response.out.write(finalText)

                totalChanged = 0
                ##check "security" of "translation"##
                for i, word in enumerate(sampleList):
                    if (not word == finalList[i]):
                        totalChanged += 1

                self.response.out.write(str(totalChanged) + "/" + str(len(sampleList)))
                percentage = 100*(float(totalChanged) / len(sampleList))
                percentage = min(100, percentage + 40)

                self.response.out.write("Safety score:" + '%.2f' % (percentage) + "%")
                self.response.out.write("=================================")


app = webapp2.WSGIApplication([('/', MainPage),
                              ('/results', Compute)],
                              debug=True)






##################################################################################################################################


##
##
##thesFile = open("thesaurus.txt")
##
##sampleText = "Hunter fared poorly at the box office at the time of its release, making only $8.6 million in the United States."
##
####Load thesaurus into dictionary with synonyms as tuples##
##
##thes = {}
##    
##for line in thesFile:
##    #print line
##    words = string.split(line)
##    tempSynonyms = []
##    firstWord = words[0] 
##    for word in words:
##        if (not word == firstWord):
##            tempSynonyms.append(word)
##    tempSynonyms = tuple(tempSynonyms)
##    thes[firstWord] = tempSynonyms
##
####Display welcome text##
##
##print ("Welcome to the Stylish Plagiariser.\n"+
##       "===================================\n"+
##       "\n"+
##       "(Enter 'q' to quit)\n")
##
##
####Create and display altered text##
##running = True
##while running:
##
##    sampleText = raw_input("\n\nPlease enter your string to be changed here:\n")
##
##    if (sampleText == 'q'):
##        print ("Thank you for using the Plagiariser.")
##        running = False;
##    else:
##        finalList = []
##        sampleList = string.split(sampleText)
##        for word in sampleList:
##            if (word in thes):
##                finalList.append(thes[word][random.randint(0,len(thes[word]) - 1)])
##            else:
##                finalList.append(word)
##        finalText = string.join(finalList, " ")
##        
##        print ("\n\nPlagiarised:")
##        print (finalText)
##
##        totalChanged = 0
##        ##check "security" of "translation"##
##        for i, word in enumerate(sampleList):
##            if (not word == finalList[i]):
##                totalChanged += 1
##
##        print (str(totalChanged) + "/" + str(len(sampleList)))
##        percentage = 100*(float(totalChanged) / len(sampleList))
##        percentage = min(100, percentage + 40)
##
##        print ("Safety score:" + '%.2f' % (percentage) + "%")
##        print ("=================================")
##
##
