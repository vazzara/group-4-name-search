import re

firstname_file = open("./texts/firstnames.csv")
firstname_text = firstname_file.read()
firstname_file.close()

firstnamesMaster = re.findall('[A-Z][A-Z]+',firstname_text,flags=0)

lastname_file = open("./texts/lastnames.csv")
lastname_text = lastname_file.read()
lastname_file.close()

lastnamesMaster = re.findall('[A-Z][A-Z]+',lastname_text,flags=0)

honorificsMaster = ["Dr.", "Mr.", "Mrs.", "Ms.", "Doctor", "Captain", "Coach", "Officer", "Reverend", "Father", "Professor", "Sir", "King", "Queen"]

numfirstnames = 0
numlastnames = 0
numfullnames = 0

firstnamesInText = [] 
lastnamesInText = []
fullnamesInText = {}
    

#Same method, but more useful for large texts because it does not print out every step.
def findNames1(text):
    #split the text into a list of words.
    textList = text.split()
    #The variable i will keep our place.
    i = 0
    #The variable l will be used later to increment i. 
    l = 0
    #This variable will be used to mark each finalized full name that is found.
    finalfullname = ""
    while (i < len(textList)):
        currentWord = textList[i]
        #resets l
        l = 0
        #boolean variables
        firstnameFlag = currentWord.upper() in firstnamesMaster and (currentWord.upper() != "AN") and currentWord[0].isupper()
        honorificsFlag = (currentWord in honorificsMaster) and (not firstnameFlag)
    
        #checks if the currentWord is a first name.
        if (firstnameFlag or honorificsFlag):
            #adds that first name to our list of first names in the text.
            endOfFirstWord = len(currentWord)
            if (firstnameFlag and currentWord not in firstnamesInText):
                firstnamesInText.append(currentWord)
                
            #regular expression that includes this first name plus any capitalized
            #names after it (gets the full name, if there is one). 
            regex = "(" +  currentWord + "((\s[A-Z][a-z]+)+)" + ")"

            #this part isolates the longest version of the full name that is found, in three steps.
            step1 = (re.findall(regex,text,flags=0))
            #print "Step 1:"
            #print step1
            if step1:
                step2 = step1.pop()
                #print "Step 2:"
                #print step2
                step3 = step2[0]
                #print "Step 3:"
                #print step3
                if (step3 not in fullnamesInText.keys()):
                    finalfullname = step3
                    if (honorificsFlag == True):
                        fullnameToAppend = step3[endOfFirstWord+1:]
                    else:
                        lastnamesInText.append(step3[endOfFirstWord+1:])
                        fullnameToAppend = step3

                    if (fullnameToAppend not in fullnamesInText.keys()):
                        fullnamesInText[fullnameToAppend]=[fullnameToAppend,1]
                    elif fullnameToAppend in fullnamesInText.keys():
                        fullnamesInText[fullnameToAppend][1]+=1
                    #this part determines the length of the full name, and then skips over the entire thing,
                    #so that segments of the full name are not mistaken as full names.
                    for n in finalfullname:
                        if n == " ":
                            l = l+1
        l = l+1
        i = i+l
    return fullnamesInText
 

# to call function call getNames(text)
# then fullnamesInText will be a list of the full names
