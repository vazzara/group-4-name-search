import re

#file = open("janeausten.txt", "r")
def readfile(filename)
    file = open(filename, "r")
    text = file.read()
    file.close()
    
text =""
names = []
with open("names_list.txt") as f:
    for line in f:
        names.append(line.split()[0].capitalize())
file.close()

extras = ["Mister", "Mr.", "Mrs.", "Ms.", "Master"]
for item in extras:
    names.append(item)

#test prints
#print(text[:100])
#print names[:10]

def namesearch(filename)
    readfile(filename)
    search = ""
    results = []
    for item in names:
        #print item
        search = "(" + item + " ([A-Z]\.)* ([A-Z][a-z]+)*)"
        L = re.findall(search, text)
        if (L != [] and L not in results):
            results.append(L[0]);
    return results


#call namesearch(filename) and it returns a list of names
