import google
import re
from bs4 import BeautifulSoup

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

def name_occurrence(text):
    names = []
    with open("names_list.txt") as f:
        for line in f:
            names.append(line.split()[0].capitalize())

    extras = ["Mister", "Mr.", "Mrs.", "Ms.", "Master", "Dr.", "Doctor", "President"]
    for item in extras:
        names.append(item)

    #test prints
    #print(text[:100])
    #print names[:10]

    search = ""
    results = []
    for item in names:
        #print item
        search = r"(([A-Z][a-z-]+){1,2}\s){2,3}"
        L = re.findall(search,  text)
        if (L != []):
            results.append(L[0]);
    print "Parsed names!"
    print results

def analyse_list(namesList):
    #takes list of names, returns analysis + answer to question
    results = {"First Result":5000,"Second Result":2000,"Third Result":1000}
    return results

def get_analysis(q):
    return analyze_list(name_occurence(parse_urls(search(q))))

if __name__ == "__main__":
    urlsList = search("Who is the President of the United States?")
    name_occurrence(parse_urls(urlsList))
