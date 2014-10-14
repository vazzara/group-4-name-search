import google
import re
from bs4 import BeautifulSoup
import namefinder1

def search(q):
    #takes question q, returns list of urls
    urlsList = []
    for url in google.search(q,tld='com',lang='en',num=10,start=0,stop=20):
        urlsList.append(url)
    print "Generated URL list!"

    return urlsList

def parse_urls(urlsList):
    #takes list of urls, returns only text
    #beautiful soup
    html = ""
    for u in urlsList:
        content = google.get_page(u)
        soup = BeautifulSoup(content)
        html += soup.get_text()
    print "Parsed HTML code!"
    return html

def name_occurence(text):
    #names1 = namefinder1.findNames1(text)
    names1 = {}
    for m in re.finditer(r"(([A-Z][a-z-]+){1,2}\s){2,3}", text):
        possiblename = ( '%s' % (m.group(0)) ).replace("\n"," ")
        if possiblename[-1] == " ": # gets rid of trailing whitespace
            possiblename = possiblename[:-1]

        if possiblename in names1.keys():
            names1[possiblename] += 1
        else:
            names1[possiblename] = 0
    print "Detected possible names!"
    return names1

def analyze_list(namesList):
    #takes list of names, returns analysis + answer to question
    top5 = []
    print namesList
    for item in namesList:
        if len(top5)<=5:
            top5.append([item,namesList[item]])
        else:
          inserted = False
          for x in range(len(top5)):
            if namesList[item] > top5[x][1] and not inserted:
                top5.insert(x, [item,namesList[item]])
                inserted = True
          top5 = top5[0:4]

    for x in range(len(top5)):
      top5[x] = "" + top5[x][0] + " : " + str(top5[x][1])
    print "Completed analysis!"
    return top5

def get_analysis(q):
    names = analyze_list(name_occurence(parse_urls(search(q))))
    return names

if __name__ == "__main__":
    print get_analysis("Who is the President of the United States?")
