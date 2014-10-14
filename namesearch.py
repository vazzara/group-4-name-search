import google
import re
from bs4 import BeautifulSoup
import namefinder1

names1 = {}

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
    names1 = namefinder1.findNames1(text)
    return names1

def analyse_list(namesList):
    #takes list of names, returns analysis + answer to question
    max_occurence = ['string',0]
    for item in namesList:
        if (item[1]>max_occurence[1]):
            max_occurence=item
    return max_occurence[0]

def get_analysis(q):
    return analyze_list(name_occurence(parse_urls(search(q))))

if __name__ == "__main__":
    print get_analysis("Who is the President of the United States?")

