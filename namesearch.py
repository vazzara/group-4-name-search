import google
from bs4 import BeautifulSoup

def search(q):
    #takes question q, returns list of urls
    print ""

def parse_urls(urlsList):
    #takes list of urls, returns only text
    #beautiful soup
    html = ""
    for u in urlsList:
        content = google.get_page(u)
        soup = BeautifulSoup(content)
        html += soup.get_text()
    return html
 
#def name_occurrence(text):
    #finds names in text

#def analyse_list(namesList):
    #takes list of names, returns analysis + answer to question


parse_urls(["http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/"])
